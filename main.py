from fastapi import FastAPI
from routes.book_route import book_router
from routes.anime_route import anime_router
from sql.database import Base, engine  # <-- important

app = FastAPI(
    title="Simple Book & Anime Management API using FastAPI & SQLAlchemy",
    version="1.0.0"
)

# 🛠️ Create tables in the PostgreSQL database on startup
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Welcome to the Book Management API. Visit /docs to explore!"}


# Register routes
app.include_router(book_router)
app.include_router(anime_router)


# To run the app, use the command: uvicorn main:app --reload