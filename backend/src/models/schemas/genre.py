from typing import Annotated, Optional

from pydantic import Field

from src.config.manager import constants
from src.models.schemas.base import BaseSchemaModel


class GenreBase(BaseSchemaModel):
    title: Annotated[
        str, Field(min_length=1, max_length=constants.MAX_TITLE_LENGTH)
    ]
    slug: Annotated[
        str, Field(min_length=1, max_length=constants.MAX_SLUG_LENGTH)
    ]


class GenreCreate(GenreBase):
    pass


class GenreUpdate(GenreCreate):
    title: Optional[str] = Field(None, min_length=1, max_length=constants.MAX_TITLE_LENGTH)
    slug: Optional[str] = Field(None, min_length=1, max_length=constants.MAX_SLUG_LENGTH)


class GenreRead(GenreBase):
    id: int