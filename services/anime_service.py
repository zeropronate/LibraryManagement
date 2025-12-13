from sqlalchemy.orm import Session
from sql import crud


def list_anime(db: Session):
    return crud.get_animes(db)


def get_anime(db: Session, anime_id: int):
    return crud.get_anime(db, anime_id)


def create_anime(db: Session, data: dict):
    return crud.create_anime(db, data)


def update_anime(db: Session, anime_id: int, update: dict):
    return crud.update_anime(db, anime_id, update)


def delete_anime(db: Session, anime_id: int):
    return crud.delete_anime(db, anime_id)
