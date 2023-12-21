from typing import Any, Optional, Sequence
from uuid import UUID

from fastapi import encoders
from sqlalchemy import Label
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, case, func, select

from src.models.db import Genre, Movie, WatchList
from src.models.schemas.movie import MovieCreate, MovieUpdate
from src.repository.crud.base import BaseCRUDRepository
from src.utils.exceptions.database import EntityNotExists
from src.utils.tools import create_image_from_bytes, generate_slug


class MovieCRUDRepository(BaseCRUDRepository[Movie, MovieCreate, MovieUpdate]):
    async def read_all(
        self, session: AsyncSession, user_id: Optional[UUID] = None, hide_watched: bool = False
    ) -> Sequence[Movie]:
        stmt = select(Movie, self._is_watched_stmt).outerjoin(
            WatchList,
            and_(Movie.id == WatchList.movie_id, WatchList.user_id == user_id),
        )

        query = await session.execute(stmt)
        results = query.unique().all()

        movies = []
        for movie, is_watched in results:
            if hide_watched and not is_watched:
                movies.append(movie)
            if not hide_watched:
                movie.is_watched = is_watched
                movies.append(movie)
        return movies

    async def read_one(
        self,
        session: AsyncSession,
        by_field: Optional[str] = None,
        value: Optional[str | int] = None,
        user_id: Optional[UUID] = None,
    ) -> Movie:
        stmt = select(Movie, self._is_watched_stmt).outerjoin(
            WatchList,
            and_(Movie.id == WatchList.movie_id, WatchList.user_id == user_id),
        )

        if by_field and value:
            stmt = stmt.where(getattr(Movie, by_field) == value)
        else:
            stmt = stmt.order_by(func.random())

        query = await session.execute(stmt)
        result = query.unique().first()
        if not result:
            raise EntityNotExists(value)

        movie, is_watched = result
        movie.is_watched = is_watched
        return movie

    async def create(
        self,
        session: AsyncSession,
        input_object: MovieCreate,
        genres: Sequence[Genre],
    ) -> Movie:
        db_object = Movie(
            **input_object.model_dump(exclude={"genres", "poster"}),
            slug=generate_slug(input_object.title, include_uuid=True),
            genres=genres
        )
        if input_object.poster:
            poster_name = await create_image_from_bytes(input_object.poster)
            db_object.poster = poster_name
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def update(
        self,
        session: AsyncSession,
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
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    @property
    def _is_watched_stmt(self) -> Label[Any]:
        return case((WatchList.movie_id != None, True), else_=False).label(
            "is_watched"
        )


movie_repo: MovieCRUDRepository = MovieCRUDRepository(Movie)
