from typing import Annotated, Optional

from pydantic import Field

from src.config.manager import constants
from src.models.schemas.base import BaseSchemaModel


class CountryBase(BaseSchemaModel):
    title: Annotated[
        str, Field(min_length=1, max_length=constants.MAX_TITLE_LENGTH)
    ]
    slug: Annotated[
        str, Field(min_length=1, max_length=constants.MAX_SLUG_LENGTH)
    ]


class CountryCreate(CountryBase):
    pass


class CountryUpdate(CountryCreate):
    title: Optional[str] = Field(None, min_length=1, max_length=constants.MAX_TITLE_LENGTH)
    slug: Optional[str] = Field(None, min_length=1, max_length=constants.MAX_SLUG_LENGTH)


class CountryRead(CountryBase):
    id: int