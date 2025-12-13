from sql import crud
from sqlalchemy.orm import Session
from fastapi import HTTPException

def list_book(db: Session):
    return crud.get_all_book(db)


def get_book(db: Session, book_id: int):
    return crud.get_book_by_id(db, book_id)


def create_book(db: Session, book_data: dict):
    try:
        new_book = crud.create_book(db, book_data)
        if book_data.get("genre")=="X":
            anime_data={
                "title": f"{new_book.title} Anime",
                "studio": "Studio",
                "genre": "X",
                "year": new_book.year,
                "book_id": new_book.id,
                #"imdb_rating": 0,
                "episodes_no": 1,
                "available": True
            }
            crud.create_anime(db, anime_data)
        return new_book

    except Exception as e:
        raise HTTPException(status_code= 500, detail=str(e))



def update_book(db: Session, book_id: int, updated_book_data: dict):
    return crud.update_book(db, book_id, updated_book_data)


def delete_book(db: Session, book_id: int):
    return crud.delete_book(db, book_id)

