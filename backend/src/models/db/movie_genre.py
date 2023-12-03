from sqlalchemy import Column, ForeignKey, Table

from src.repository.table import Base

movie_genre = Table(
    "movie_genre",
    Base.metadata,
    Column(
        "movie_id",
        ForeignKey("movie.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "genre_id",
        ForeignKey("genre.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
