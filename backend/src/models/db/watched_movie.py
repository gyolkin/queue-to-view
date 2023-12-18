from sqlalchemy import Column, ForeignKey, Table

from src.repository.table import Base

watched_movie = Table(
    "watched_movie",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("movie_id", ForeignKey("movie.id"), primary_key=True),
)
