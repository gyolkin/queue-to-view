from fastapi import FastAPI
from loguru import logger
from sqlalchemy import event
from sqlalchemy.dialects.postgresql.asyncpg import (
    AsyncAdapt_asyncpg_connection,
)
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.pool.base import _ConnectionRecord

from src.repository.database import async_db
from src.repository.table import Base


@event.listens_for(
    target=async_db.async_engine.sync_engine, identifier="connect"
)
def inspect_db_server_on_connection(
    db_api_connection: AsyncAdapt_asyncpg_connection,
    connection_record: _ConnectionRecord,
) -> None:
    logger.info(f"New DB API Connection ---\n {db_api_connection}")
    logger.info(f"Connection Record ---\n {connection_record}")


@event.listens_for(
    target=async_db.async_engine.sync_engine, identifier="close"
)
def inspect_db_server_on_close(
    db_api_connection: AsyncAdapt_asyncpg_connection,
    connection_record: _ConnectionRecord,
) -> None:
    logger.info(f"Closing DB API Connection ---\n {db_api_connection}")
    logger.info(f"Closed Connection Record ---\n {connection_record}")


async def initialize_db_tables(connection: AsyncConnection) -> None:
    logger.info("Database Table Creation --- Initializing . . .")
    await connection.run_sync(Base.metadata.create_all)
    logger.info("Database Table Creation --- Successfully Initialized!")


async def initialize_db_connection(backend_app: FastAPI) -> None:
    logger.info("Database Connection --- Establishing . . .")
    backend_app.state.db = async_db
    async with backend_app.state.db.async_engine.begin() as connection:
        await initialize_db_tables(connection=connection)
    logger.info("Database Connection --- Successfully Established!")


async def dispose_db_connection(backend_app: FastAPI) -> None:
    logger.info("Database Connection --- Disposing . . .")
    await backend_app.state.db.async_engine.dispose()
    logger.info("Database Connection --- Successfully Disposed!")
