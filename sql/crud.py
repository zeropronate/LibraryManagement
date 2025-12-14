from sqlalchemy.orm import Session
from .models import Book,Anime

# ---------------- BOOK CRUD ----------------

def get_all_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: Book):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book_by_id(db: Session, book_id: int, data: dict):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None

    for key, value in data.items():
            setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book: Book):
    db.delete(book)
    db.commit()

def get_all_anime(db: Session):
    return db.query(Anime).all()

def create_anime(db: Session, anime: Anime):
    db.add(anime)
    db.commit()
    db.refresh(anime)
    return anime


def delete_anime(db: Session, anime: Anime):
    db.delete(anime)
    db.commit()


def get_anime_by_id(db: Session, anime_id: int):
    return db.query(Anime).filter(Anime.id == anime_id).first()

def update_anime_by_id(db: Session, anime_id: int, data: dict):
    anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if not anime:
        return None

    # apply only keys provided in the incoming data dict
    for key, value in data.items():
            setattr(anime, key, value)

    db.commit()
    db.refresh(anime)
    return anime