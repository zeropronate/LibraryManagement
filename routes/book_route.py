from fastapi import APIRouter, Depends
from services.book_service import list_book, get_book_by_id, create_book, update_book, delete_book
from sql.database import get_db

book_router = APIRouter(prefix="/book", tags=["books"])

@book_router.get("/", summary="List all books")
def list_all(db = Depends(get_db)):
    return list_book(db)

@book_router.get("/{book_id}",)
def single_book(book_id: int,db = Depends(get_db)):
    book = get_book_by_id(db, book_id)
    if book:
        return book
    else:
        return {"error": "Book not found"}

@book_router.post("/", summary="Create a new book")
def add_book(data: dict,db = Depends(get_db)):
    try:
        book = create_book(db,data)
        return book
    except Exception as e:
        return {"error": str(e)}

@book_router.put("/{book_id}", summary="Update a book")
def modify_book(book_id: int, data: dict,db = Depends(get_db)):
    updated_book = update_book(db, book_id, data)
    if updated_book:
        return updated_book
    else:
        return{"error": "Book not found"}


@book_router.delete("/{book_id}", summary="Delete a book")
def remove_book(book_id: int,db = Depends(get_db)):
    deleted = delete_book(db, book_id)
    if deleted:
        return {"message": "Book deleted successfully"}
    else:
        return {"error": "Book not found"}
