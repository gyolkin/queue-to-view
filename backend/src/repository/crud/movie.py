from typing import Optional, Sequence

from fastapi import encoders
from sqlalchemy.sql import and_, func, select

from src.models.db import Genre, Movie, User, watched_movie
from src.models.schemas.movie import MovieCreate, MovieUpdate
from src.repository.crud.base import BaseCRUDRepository
from src.utils.exceptions.database import EntityNotExists
from src.utils.tools import create_image_from_bytes, generate_slug


class MovieCRUDRepository(BaseCRUDRepository[Movie, MovieCreate, MovieUpdate]):
    async def read_one(
        self,
        user: Optional[User] = None,
        by_field: Optional[str] = None,
        value: Optional[str | int] = None,
    ) -> Movie:
        stmt = select(Movie)
        if by_field and value:
            stmt = stmt.where(getattr(Movie, by_field) == value)
        else:
            stmt = stmt.order_by(func.random())
        query = await self.async_session.execute(stmt)
        movie = query.scalars().first()

        if not movie:
            raise EntityNotExists(value)

        if user:
            watched_stmt = select(watched_movie.c.movie_id).where(
                and_(
                    watched_movie.c.movie_id == movie.id,
                    watched_movie.c.user_id == user.id,
                )
            )
            watched_query = await self.async_session.execute(watched_stmt)
            movie.is_watched = watched_query.scalar() is not None
        return movie

    async def read_all(self, user: Optional[User] = None) -> Sequence[Movie]:
        stmt = select(Movie)
        query = await self.async_session.execute(stmt)
        movies = query.scalars().all()

        if user:
            # todo: optimize
            watched_stmt = select(watched_movie.c.movie_id).where(
                watched_movie.c.user_id == user.id
            )
            watched_query = await self.async_session.execute(watched_stmt)
            watched_movie_ids = {row[0] for row in watched_query.fetchall()}
            for movie in movies:
                movie.is_watched = movie.id in watched_movie_ids
        return movies

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
