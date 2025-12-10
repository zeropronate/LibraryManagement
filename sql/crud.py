from sqlalchemy.orm import Session
from .models import Book, Anime

# CRUD of book

def get_all_book(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: dict):
    new_book = Book(**book)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update_book(db: Session, book_id: int, data: dict):
    existing_book = get_book_by_id(db, book_id)
    if not existing_book:
        return None

    # apply only keys provided in the incoming data dict
    for key, value in data.items():
        # avoid setting attributes that don't exist on the model
        if hasattr(existing_book, key):
            setattr(existing_book, key, value)

    db.commit()
    db.refresh(existing_book)
    return existing_book

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book

# CRUD of anime

def get_all_anime(db: Session):
    return db.query(Anime).all()

def get_anime_by_id(db: Session, anime_id: int):
    return db.query(Anime).filter(Anime.id == anime_id).first()

def get_anime_by_book_id(db: Session, book_id: int):
    return db.query(Anime).filter(Anime.book_id == book_id).first()

def create_anime(db: Session, anime: dict):
    new_anime = Anime(**anime)
    db.add(new_anime)
    db.commit()
    db.refresh(new_anime)
    return new_anime

def update_anime(db: Session, anime_id: int, data: dict):
    existing_anime = get_anime_by_id(db, anime_id)
    if not existing_anime:
        return None

    for key, value in data.items():
        if hasattr(existing_anime, key):
            setattr(existing_anime, key, value)

    db.commit()
    db.refresh(existing_anime)
    return existing_anime

def delete_anime(db: Session, anime_id: int):
    anime = get_anime_by_id(db, anime_id)
    if not anime:
        return None
    db.delete(anime)
    db.commit()
    return anime
