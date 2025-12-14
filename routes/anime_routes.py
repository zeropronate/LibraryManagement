from fastapi import APIRouter, Depends
from services.anime_service import get_anime, create_anime, update_anime, delete_anime,list_anime
from sql.database import get_db

anime_router = APIRouter(prefix="/anime", tags=["anime"])

@anime_router.get("/", summary="List all anime")
def list_all(db = Depends(get_db)):
    try:
        return list_anime(db)
    except Exception as e:
        return {"error": str(e)}

@anime_router.get("/{anime_id}",)
def single_anime(anime_id: int,db = Depends(get_db)):
    try:
        anime = get_anime(db, anime_id)
        if anime:
            return anime
        else:
            return {"error": "anime not found"}
    except Exception as e:
        return {"error": str(e)}

@anime_router.post("/", summary="Create a new anime")
def add_anime(data: dict,db = Depends(get_db)):
    try:
        return create_anime(db,data)
    except Exception as e:
        return {"error": str(e)}


@anime_router.put("/{anime_id}", summary="Update a anime")
def modify_anime(anime_id: int, data: dict,db = Depends(get_db)):
    try:
        updated_anime = update_anime(db, anime_id, data)
        if updated_anime:
            return updated_anime
        else:
            return{"error": "anime not found"}
    except Exception as e:
        return {"error": str(e)}



@anime_router.delete("/{anime_id}", summary="Delete a anime")
def remove_anime(anime_id: int,db = Depends(get_db)):
    try:
        deleted = delete_anime(db, anime_id)
        if deleted:
            return {"message": "anime deleted successfully"}
        else:
            return {"error": "anime not found"}
    except Exception as e:
        return {"error": str(e)}
