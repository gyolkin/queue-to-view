from typing import Any

from fastapi import FastAPI
from loguru import logger

from src.repository.events import (
    dispose_db_connection,
    initialize_db_connection,
)


def execute_backend_server_event_handler(
    backend_app: FastAPI,
) -> Any:
    async def launch_backend_server_events() -> None:
        await initialize_db_connection(backend_app=backend_app)

    return launch_backend_server_events


def terminate_backend_server_event_handler(
    backend_app: FastAPI,
) -> Any:
    @logger.catch
    async def stop_backend_server_events() -> None:
        await dispose_db_connection(backend_app=backend_app)

    return stop_backend_server_events
