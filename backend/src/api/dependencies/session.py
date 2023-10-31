from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession

from src.repository.database import async_db


async def get_async_session() -> AsyncGenerator[SQLAlchemyAsyncSession, None]:
    try:
        yield async_db.async_session
    except Exception:
        await async_db.async_session.rollback()
    finally:
        await async_db.async_session.close()
