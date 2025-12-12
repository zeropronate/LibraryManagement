from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base

COLUMNS = ["id", "title", "author", "genre", "year", "available"]


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