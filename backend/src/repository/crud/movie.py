from typing import Optional, Sequence

from fastapi import encoders

from src.models.db import Genre, Movie
from src.models.schemas.movie import MovieCreate, MovieUpdate
from src.repository.crud.base import BaseCRUDRepository
from src.utils.tools import create_image_from_bytes, generate_slug


class MovieCRUDRepository(BaseCRUDRepository[Movie, MovieCreate, MovieUpdate]):
    async def create(
        self, input_object: MovieCreate, genres: Sequence[Genre]
    ) -> Movie:
        db_object = Movie(
            **input_object.model_dump(exclude={"genres", "poster"}),
            slug=generate_slug(input_object.title, include_uuid=True),
            genres=genres
        )
        if input_object.poster:
            poster_name = await create_image_from_bytes(input_object.poster)
            db_object.poster = poster_name
        self.async_session.add(db_object)
        await self.async_session.commit()
        await self.async_session.refresh(db_object)
        return db_object

    async def update(
        self,
        db_object: Movie,
        input_object: MovieUpdate,
        genres: Optional[Sequence[Genre]],
    ) -> Movie:
        current_data = encoders.jsonable_encoder(db_object)
        updated_data = input_object.model_dump(
            exclude_unset=True, exclude={"genres", "poster"}
        )
        if input_object.genres:
            updated_data["genres"] = genres
        if input_object.poster:
            poster_name = await create_image_from_bytes(input_object.poster)
            updated_data["poster"] = poster_name
        if "title" in updated_data:
            updated_data["slug"] = generate_slug(
                updated_data["title"], include_uuid=True
            )
        for field in current_data:
            if field in updated_data:
                setattr(db_object, field, updated_data[field])
        self.async_session.add(db_object)
        await self.async_session.commit()
        await self.async_session.refresh(db_object)
        return db_object
