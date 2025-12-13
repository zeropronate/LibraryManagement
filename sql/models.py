from sqlalchemy import Column, Integer, String, Boolean, Text
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


# ------------------------
# New: Anime model
# ------------------------
class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, unique=True, index=True)
    genre = Column(String(100), nullable=True)
    studio = Column(String(100), nullable=True)
    episodes = Column(Integer, nullable=True)
    rating = Column(String(20), nullable=True)
    description = Column(Text, nullable=True)
