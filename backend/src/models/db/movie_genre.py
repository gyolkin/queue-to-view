from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from src.repository.table import Base


class MovieGenre(Base):
    movie_id = mapped_column(
        ForeignKey("movie.id", ondelete="CASCADE"), primary_key=True
    )
    genre_id = mapped_column(
        ForeignKey("genre.id", ondelete="CASCADE"), primary_key=True
    )
