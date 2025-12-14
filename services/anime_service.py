from sql import crud
from sql.models import Book, Anime
from sqlalchemy.orm import Session

def list_anime(db: Session):
    return crud.get_all_anime(db)

def get_anime(db: Session, anime_id: int):
    return crud.get_anime_by_id(db, anime_id)


def create_anime(db: Session, data: dict):
    anime = Anime(**data)
    return crud.create_anime(db, anime)


def update_anime(db: Session, anime_id: int, update: dict):

    #Buisness logic: imdb rating decides the book availability and the anime's no of episodes
    if "imdb_rating" in update or update["imdb_rating"] is not None:
        rating = update["imdb_rating"]
        anime = crud.get_anime_by_id(db, anime_id)
        book = anime.book
        updated_aval_book = 0
        if rating < 5:
            #book's available status becomes false if rating is below 5
            if book:
               updated_aval_book = dict(available = False)
        elif 5 < rating <= 8:
            if book:
                # book's available status becomes true if rating is between 5 and 8
                updated_aval_book = dict(available = True)
        else:
            #if rating is above 8, increase no of episodes by 100%
            if anime:
                new_episodes = int(anime.no_of_episodes * 2)
                update["no_of_episodes"] = new_episodes
        if updated_aval_book:
            crud.update_book_by_id(db, book.id, updated_aval_book)
    return crud.update_anime_by_id(db, anime_id, update)


def delete_anime(db: Session, anime_id: int):
    anime = crud.get_anime_by_id(db, anime_id)

    if not anime:
        return None
    #Buisness logic: When deleting an anime, also delete the associated book if it exists
    if anime.genre == "X":
        book = anime.book
        crud.delete_book(db, book)

    crud.delete_anime(db, anime)
    return True