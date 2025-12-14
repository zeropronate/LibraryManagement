from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base



class Book(Base):
    __tablename__ = "Book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

    #One book can have multiple animes :L Mapper
    anime = relationship("Anime", back_populates="book", cascade="all, delete-orphan")


class Anime(Base):
    __tablename__ = "Anime"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    studio = Column(String, nullable=True)
    episodes = Column(Integer, nullable=True)
    ongoing = Column(Boolean, default=True)

    book_id = Column(Integer, ForeignKey("Book.id", ondelete="CASCADE"), nullable= False)

    #mapper to book
    book = relationship("Book", back_populates="anime")