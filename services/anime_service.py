from sql import crud
from sqlalchemy.orm import Session


def list_anime(db: Session):
    return crud.get_all_anime(db)


def get_anime(db: Session, anime_id: int):
    return crud.get_anime_by_id(db, anime_id)


def get_anime_by_book_id(db: Session, book_id: int):
    return crud.get_anime_by_book_id(db, book_id)


def create_anime(db: Session, anime_data: dict):
    return crud.create_anime(db, anime_data)


def update_anime(db: Session, anime_id: int, updated_anime_data: dict):
    return crud.update_anime(db, anime_id, updated_anime_data)


def delete_anime(db: Session, anime_id: int):
    return crud.delete_anime(db, anime_id)