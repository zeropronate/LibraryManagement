from fastapi import APIRouter, Depends
from services.anime_service import (
    list_anime,
    get_anime,
    create_anime,
    update_anime,
    delete_anime,
)
from sql.database import get_db

anime_router = APIRouter(prefix="/anime", tags=["anime"])


@anime_router.get("/", summary="List all anime")
def list_all(db=Depends(get_db)):
    return list_anime(db)


@anime_router.get("/{anime_id}")
def single_anime(anime_id: int, db=Depends(get_db)):
    anime = get_anime(db, anime_id)
    if anime:
        return anime
    else:
        return {"error": "Anime not found"}


@anime_router.post("/", summary="Create a new anime")
def add_anime(data: dict, db=Depends(get_db)):
    return create_anime(db, data)


@anime_router.put("/{anime_id}", summary="Update an anime")
def modify_anime(anime_id: int, data: dict, db=Depends(get_db)):
    updated = update_anime(db, anime_id, data)
    if updated:
        return updated
    else:
        return {"error": "Anime not found"}


@anime_router.delete("/{anime_id}", summary="Delete an anime")
def remove_anime(anime_id: int, db=Depends(get_db)):
    deleted = delete_anime(db, anime_id)
    if deleted:
        return {"message": "Anime deleted successfully"}
    else:
        return {"error": "Anime not found"}
