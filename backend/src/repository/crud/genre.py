from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from src.models.db import Genre
from src.models.schemas.genre import GenreCreate, GenreUpdate
from src.repository.crud.base import BaseCRUDRepository


class GenreCRUDRepository(BaseCRUDRepository[Genre, GenreCreate, GenreUpdate]):
    async def read_by_id_list(
        self, session: AsyncSession, id_list: list[int]
    ) -> Sequence[Genre]:
        query = select(Genre).where(Genre.id.in_(id_list))
        result = await session.execute(query)
        return result.scalars().all()


genre_repo: GenreCRUDRepository = GenreCRUDRepository(Genre)
