from fastapi import FastAPI
from sql.database import Base, engine  # <-- important
from routes.book_route import book_router
from routes.anime_route import anime_router

app = FastAPI(
    title="Simple Book Management API using FastAPI & SQLAlchemy",
    version="1.0.0"
)

# 🛠️ Create tables in the PostgreSQL database on startup
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Welcome to the Book Management API. Visit /docs to explore!"}


# Register routes
app.include_router(book_router)
app.include_router(anime_router)
