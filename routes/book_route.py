from fastapi import APIRouter, Depends, HTTPException
from services.book_service import list_book, get_book, create_book, update_book, delete_book
from sql.database import get_db

book_router = APIRouter(prefix="/book", tags=["books"])


@book_router.get("/", summary="List all books")
def list_all_book(db=Depends(get_db)):
    return list_book(db)


@book_router.get("/{book_id}", summary="Get book by ID")
def single_book(book_id: int, db=Depends(get_db)):
    book = get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.post("/", summary="Create a new book")
def add_book(book_data: dict, db=Depends(get_db)):
    return create_book(db, book_data)


@book_router.put("/{book_id}", summary="Update a book")
def modify_book(book_id: int, book_data: dict, db=Depends(get_db)):
    updated_book = update_book(db, book_id, book_data)

    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@book_router.delete("/{book_id}", summary="Delete a book")
def remove_book(book_id: int, db=Depends(get_db)):
    deleted = delete_book(db, book_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book is deleted successfully (any linked annime is now unlinked)"}
