from sql import crud
from sqlalchemy.orm import Session


def list_book(db: Session):
    return crud.get_all_book(db)


def get_book(db: Session, book_id: int):
    return crud.get_book_by_id(db, book_id)


def create_book(db: Session, book_data: dict):
    return crud.create_book(db, book_data)


def update_book(db: Session, book_id: int, updated_book_data: dict):
    return crud.update_book(db, book_id, updated_book_data)


def delete_book(db: Session, book_id: int):
    return crud.delete_book(db, book_id)

