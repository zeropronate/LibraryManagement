from fastapi import HTTPException
from sql import crud
from sqlalchemy.orm import Session

from sql.crud import get_anime_by_id


def list_anime(db: Session):
    return crud.get_all_anime(db)


def get_anime(db: Session, anime_id: int):
    return crud.get_anime_by_id(db, anime_id)


def create_anime(db: Session, anime_data: dict):
    return crud.create_anime(db, anime_data)


def update_anime(db: Session, anime_id: int, updated_anime_data: dict):
    anime = get_anime_by_id(db, anime_id)
    if not anime:
        raise Exception("Anime not found")
    else:
        if "imdb_rating" in updated_anime_data and updated_anime_data["imdb_rating"] is not None:
            try:
                rating = float(updated_anime_data["imdb_rating"])
            except ValueError:
                raise Exception("Invalid IMDb rating")
            if rating < 5:
                anime.available = False

            elif 5 <= rating <= 7:
                anime.available = True

            elif rating > 7:
                anime.episodes_no *= 2
    return crud.update_anime(db, anime_id, updated_anime_data)


def delete_anime(db: Session, anime_id: int):
    try:
        anime = crud.get_anime_by_id(db, anime_id)
        if not anime:
            raise HTTPException(status_code=404, detail="Anime not found")

        deleted_anime = crud.delete_anime(db, anime_id)

        if anime.genre == "X":
            crud.delete_book(db, anime.book_id)

        return deleted_anime

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
