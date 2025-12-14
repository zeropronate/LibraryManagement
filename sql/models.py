from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

    # One-directional relationship (NO back_populates)
    anime = relationship("Anime")


class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=True)
    production_house = Column(String, nullable=True)
    episodes_no = Column(Integer, nullable=True)
    genre = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    imdb_rating = Column(Float, nullable=True)       # ratings are not boolean
    based_on_manga = Column(Boolean, default=True)