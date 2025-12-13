from sqlalchemy.orm import Session
from .models import Book, Anime
from typing import Optional, Dict, List

# -----------------------------
# BOOK CRUD
# -----------------------------

def get_all(db: Session):
    return db.query(Book).all()

def get_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: dict):
    new_book = Book(**book)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update(db: Session, book_id: int, data: dict):
    existing = get_by_id(db, book_id)
    if not existing:
        return None

    for key, value in data.items():
        if hasattr(existing, key):
            setattr(existing, key, value)

    db.commit()
    db.refresh(existing)
    return existing

def delete(db: Session, book_id: int):
    book = get_by_id(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book


# -----------------------------
# ANIME CRUD
# -----------------------------

def get_animes(db: Session, skip: int = 0, limit: int = 100) -> List[Anime]:
    return db.query(Anime).offset(skip).limit(limit).all()

def get_anime(db: Session, anime_id: int) -> Optional[Anime]:
    return db.query(Anime).filter(Anime.id == anime_id).first()

def get_anime_by_title(db: Session, title: str) -> Optional[Anime]:
    return db.query(Anime).filter(Anime.title == title).first()

def create_anime(db: Session, anime_data: Dict) -> Anime:
    anime = Anime(**anime_data)
    db.add(anime)
    db.commit()
    db.refresh(anime)
    return anime

def update_anime(db: Session, anime_id: int, anime_data: Dict) -> Optional[Anime]:
    anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if not anime:
        return None

    for key, value in anime_data.items():
        if hasattr(anime, key):
            setattr(anime, key, value)

    db.commit()
    db.refresh(anime)
    return anime

def delete_anime(db: Session, anime_id: int) -> Optional[Anime]:
    anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if not anime:
        return None

    db.delete(anime)
    db.commit()
    return anime
