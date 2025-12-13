from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base

BOOK_COLUMNS = ["id", "title", "author", "genre", "year", "available"]

ANIME_COLUMNS = ["id", "title", "studio", "genre", "year", "book_id", "imdb_rating", "episodes_no", "available"]

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)


class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    studio = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=True)
    imdb_rating = Column(Integer, nullable=True)
    episodes_no = Column(Integer, nullable=True)
    available = Column(Boolean, default=True)
