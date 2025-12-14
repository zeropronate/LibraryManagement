from sql import crud
from sql.crud import get_by_anime_id
from sqlalchemy.orm import Session


def list_anime(db: Session):
    return crud.get_all_anime(db)


def get_anime(db: Session, anime_id: int):
    return crud.get_by_anime_id(db, anime_id)


def create_anime(db: Session, data: dict):
    return crud.create_anime(db, data)


def update_anime(db: Session, anime_id: int, update: dict):
    anime = get_by_anime_id(db, anime_id)
    book = crud.get_by_book_id(db, anime.book_id)
    if not anime:
        raise Exception("Anime not found")
    else:
        if update["imdb_rating"] is not None:
                rating = update["imdb_rating"]
                if rating < 5:
                        book.available = False
                        return crud.update_book()
                elif 5 <= rating <= 7:
                        book.available = True
                        return crud.update_book()
                elif rating > 7:
                        anime.episodes_no = anime.episodes_no*2

    return crud.update_anime(db, anime_id, update)


def delete_anime(db: Session, anime_id: int):
    anime = get_by_anime_id(db, anime_id)
    if not anime:
        raise Exception("Anime not found")
    else:
        try:
            if anime.genre == "X":
                deleted_anime = crud.delete_anime(db, anime_id)
                return deleted_anime
            else:
                deleted_anime = crud.delete_anime(db, anime_id)
        except Exception as e:
            raise Exception(f"Error deleting an anime: {str(e)}")
    return deleted_anime