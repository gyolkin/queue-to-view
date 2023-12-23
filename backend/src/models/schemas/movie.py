import datetime
from typing import Annotated, Optional

from pydantic import Field, PositiveInt, field_validator

from src.config.manager import constants, settings
from src.models.schemas.base import BaseSchemaModel
from src.models.schemas.country import Country
from src.utils.validators import check_list_not_empty, normalize_str


class MovieBase(BaseSchemaModel):
    title: Annotated[
        str, Field(min_length=1, max_length=constants.MAX_TITLE_LENGTH)
    ]
    description: Annotated[
        str, Field(min_length=1, max_length=constants.MAX_TEXT_LENGTH)
    ]
    release_year: Annotated[
        int,
        Field(gt=constants.MIN_RELEASE_YEAR, le=constants.MAX_RELEASE_YEAR),
    ]
    duration: PositiveInt
    country: Annotated[str, Field(min_length=2, max_length=2)]
    genres: list[int]
    imdb_rating: Optional[float] = Field(None, ge=0.0, le=10.0)
    poster: Optional[bytes] = None


class MovieCreate(MovieBase):
    pass

    """Валидаторы, которые применяются для Create и Update схем."""
    normalize_str = field_validator("title", "description")(normalize_str)
    check_genres_not_empty = field_validator("genres")(check_list_not_empty)

    @field_validator("country")
    def validate_country(cls, v: str):
        try:
            getattr(Country, v)
        except AttributeError:
            raise ValueError("Нет такой страны.")
        return v


class MovieUpdate(MovieCreate):
    title: Optional[str] = Field(None, max_length=constants.MAX_TITLE_LENGTH)
    description: Optional[str] = Field(
        None, max_length=constants.MAX_TEXT_LENGTH
    )
    release_year: Optional[int] = Field(
        None, gt=constants.MIN_RELEASE_YEAR, le=constants.MAX_RELEASE_YEAR
    )
    duration: Optional[PositiveInt] = None
    genres: Optional[list[int]] = []
    country: Optional[str] = Field(None, min_length=2, max_length=2)


class MovieDetailedRead(MovieBase):
    id: int
    slug: str
    created_at: datetime.datetime
    country: Country
    genres: list["GenreRead"]
    poster: str

    @field_validator("poster")
    def convert_poster_url(cls, v: str) -> str:
        return f"{settings.get_static_folder_url}/{v}"


from .genre import GenreRead  # noqa

MovieDetailedRead.model_rebuild()
