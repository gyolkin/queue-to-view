import datetime
from typing import Annotated, Optional

from pydantic import Field, PositiveInt, field_validator

from src.config.manager import constants, settings
from src.models.schemas.base import BaseSchemaModel
from src.utils.validators import check_list_not_empty, normalize_str


class MovieBase(BaseSchemaModel):
    title: Annotated[
        str, Field(min_length=1, max_length=constants.MAX_TITLE_LENGTH)
    ]
    description: Annotated[
        str, Field(min_length=1, max_length=constants.MAX_TEXT_LENGTH)
    ]
    release_year: Annotated[int, Field(gt=1899, le=2030)]
    duration: PositiveInt
    country_id: int
    genres: list[int]
    imdb_rating: Optional[float] = Field(None, ge=0.0, le=10.0)
    poster: Optional[bytes] = None


class MovieCreate(MovieBase):
    pass

    """Валидаторы, которые применяются для Create и Update схем."""
    normalize_title_desc = field_validator("title", "description")(
        normalize_str
    )
    check_genres_not_empty = field_validator("genres")(check_list_not_empty)


class MovieUpdate(MovieCreate):
    title: Optional[str] = Field(None, max_length=constants.MAX_TITLE_LENGTH)
    description: Optional[str] = Field(
        None, max_length=constants.MAX_TEXT_LENGTH
    )
    release_year: Optional[int] = Field(None, gt=1899, le=2030)
    duration: Optional[PositiveInt] = None
    country_id: Optional[int] = None
    genres: Optional[list[int]] = None


class MovieDetailedRead(MovieBase):
    id: int
    slug: str
    created_at: datetime.datetime
    country: "CountryRead"
    genres: list["GenreRead"]
    poster: str
    country_id: int = Field(exclude=True)

    @field_validator("poster")
    def add_url_prefix(cls, v: str) -> str:
        return f"{settings.get_static_folder_url}/{v}"


from .country import CountryRead  # noqa
from .genre import GenreRead  # noqa

MovieDetailedRead.model_rebuild()
