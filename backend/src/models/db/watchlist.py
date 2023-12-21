from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from src.repository.table import Base


class WatchList(Base):
    user_id = mapped_column(ForeignKey("user.id"), primary_key=True)
    movie_id = mapped_column(ForeignKey("movie.id"), primary_key=True)
