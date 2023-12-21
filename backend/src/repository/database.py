from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.pool import Pool, QueuePool

from src.config.manager import settings


class AsyncDatabase:
    def __init__(self):
        self.postgres_uri = f"{settings.POSTGRES_SCHEMA}://{settings.POSTGRES_USERNAME}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        self.async_engine: AsyncEngine = create_async_engine(
            url=self.postgres_uri,
            poolclass=QueuePool,
        )
        self.async_session: AsyncSession = AsyncSession(bind=self.async_engine)
        self.pool: Pool = self.async_engine.pool

    def __str__(self):
        return self.postgres_uri


async_db: AsyncDatabase = AsyncDatabase()
