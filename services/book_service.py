from sql import crud
from sqlalchemy.orm import Session


def list_book(db: Session):
    return crud.get_all_books(db)


def get_book(db: Session, book_id: int):
    return crud.get_by_book_id(db, book_id)


def create_book(db: Session, data: dict):
    try:
        if data.get("genre") == "X":
            new_book = crud.create_book(db, data)
            anime_data = {
                "book_id": new_book.id,
                "genre": "X",
            }
            new_anime = crud.create_anime(db, anime_data)
        else:
            new_book = crud.create_book(db, data)
    except Exception as e:
        raise Exception(f"Error creating book: {str(e)}")
    return new_book


def update_book(db: Session, book_id: int, update: dict):
    return crud.update_book(db, book_id, update)


def delete_book(db: Session, book_id: int):
    return crud.delete_book(db, book_id)