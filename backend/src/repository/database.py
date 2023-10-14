from sqlalchemy.ext.asyncio import AsyncEngine as SQLAlchemyAsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession
from sqlalchemy.ext.asyncio import (
    create_async_engine as create_sqlalchemy_async_engine,
)
from sqlalchemy.pool import Pool as SQLAlchemyPool
from sqlalchemy.pool import QueuePool as SQLAlchemyQueuePool

from src.config.manager import settings


class AsyncDatabase:
    def __init__(self):
        self.postgres_uri = f"{settings.POSTGRES_SCHEMA}://{settings.POSTGRES_USERNAME}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        self.async_engine: SQLAlchemyAsyncEngine = (
            create_sqlalchemy_async_engine(
                url=self.postgres_uri,
                poolclass=SQLAlchemyQueuePool,
            )
        )
        self.async_session: SQLAlchemyAsyncSession = SQLAlchemyAsyncSession(
            bind=self.async_engine
        )
        self.pool: SQLAlchemyPool = self.async_engine.pool

    def __str__(self):
        return self.postgres_uri


async_db: AsyncDatabase = AsyncDatabase()
