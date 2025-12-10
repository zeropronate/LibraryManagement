from fastapi import APIRouter, Depends, HTTPException
from services.anime_service import list_anime, get_anime, create_anime, update_anime, delete_anime, get_anime_by_book_id
from sql.database import get_db

anime_router = APIRouter(prefix="/anime", tags=["anime"])


@anime_router.get("/", summary="List all anime")
def list_all_anime(db=Depends(get_db)):
    return list_anime(db)


@anime_router.get("/{anime_id}", summary="Get anime by ID")
def single_anime(anime_id: int, db=Depends(get_db)):
    anime = get_anime(db, anime_id)

    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return anime


@anime_router.get("{book_id}", summary="Get anime by book ID")
def get_anime_from_book(book_id: int, db=Depends(get_db)):
    anime = get_anime_by_book_id(db, book_id)

    if not anime:
        raise HTTPException(status_code=404, detail="No anime linked with this book")
    return anime


@anime_router.post("/", summary="Create an new anime")
def add_anime(anime_data: dict, db=Depends(get_db)):
    new_anime = create_anime(db, anime_data)

    if new_anime is None:
        raise HTTPException(status_code=400, detail="This book is already linked to another anime")
    return new_anime


@anime_router.put("/{anime_id}", summary="Update an anime")
def modify_anime(anime_id: int, anime_data: dict, db=Depends(get_db)):
    updated_anime = update_anime(db, anime_id, anime_data)

    if not updated_anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return updated_anime


@anime_router.delete("/{anime_id}", summary="Delete an anime")
def remove_anime(anime_id: int, db=Depends(get_db)):
    deleted = delete_anime(db, anime_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    elif deleted is False:
        raise HTTPException(status_code=400, detail="Cannot delete anime because it is linked with a book. Unlink it first")
    return {"message": "Anime is deleted successfully"}
