from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from src.models.db import WatchList


class WatchListCRUDRepository:
    async def read_by_movie_id(
        self, session: AsyncSession, user_id: UUID, movie_id: int
    ) -> Optional[WatchList]:
        stmt = (
            select(WatchList)
            .where(WatchList.user_id == user_id)
            .where(WatchList.movie_id == movie_id)
        )
        query = await session.execute(statement=stmt)
        return query.scalars().first()

    async def create(
        self, session: AsyncSession, user_id: UUID, movie_id: int
    ) -> WatchList:
        db_object = WatchList(user_id=user_id, movie_id=movie_id)
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def delete(
        self, session: AsyncSession, db_object: WatchList
    ) -> None:
        await session.delete(db_object)
        await session.commit()
        return None


watched_repo = WatchListCRUDRepository()
