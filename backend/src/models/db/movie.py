from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    Float,
    Integer,
    String,
    desc,
)
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.sql import functions

from src.config.manager import constants
from src.models.schemas.country import Country
from src.repository.table import AutoincrementIDMixin, Base


class Movie(Base, AutoincrementIDMixin):
    title = mapped_column(String(constants.MAX_TITLE_LENGTH), nullable=False)
    slug = mapped_column(
        String(constants.MAX_SLUG_LENGTH), unique=True, nullable=False
    )
    description = mapped_column(
        String(constants.MAX_TEXT_LENGTH), nullable=False
    )
    release_year = mapped_column(Integer, nullable=False)
    duration = mapped_column(Integer, nullable=False)
    imdb_rating = mapped_column(Float, nullable=True)
    poster = mapped_column(String, nullable=True, default="default.jpg")
    country = mapped_column(Enum(Country), nullable=False)
    created_at = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=functions.now()
    )

    genres = relationship(
        "Genre",
        secondary="movie_genre",
        back_populates="movie",
        lazy="selectin",
    )

    is_watched = False

    __table_args__ = (
        CheckConstraint(
            f"release_year >= {constants.MIN_RELEASE_YEAR} AND release_year <= {constants.MAX_RELEASE_YEAR}"
        ),
        CheckConstraint("duration > 0"),
        CheckConstraint("imdb_rating >= 0.0 AND imdb_rating <= 10.0"),
        {"order_by": desc(created_at)},
    )
