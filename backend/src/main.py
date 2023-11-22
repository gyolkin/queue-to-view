from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from src.api.endpoints import router
from src.config.events import (
    execute_backend_server_event_handler,
    terminate_backend_server_event_handler,
)
from src.config.manager import settings
from src.models.schemas.exceptions import ValidationErrorResponse
from src.utils.docs import custom_openapi
from src.utils.exceptions.handlers import validation_exception_handler


def initialize_backend_application() -> FastAPI:
    app = FastAPI(
        **settings.set_backend_app_attributes,  # type: ignore
        responses={
            status.HTTP_422_UNPROCESSABLE_ENTITY: {
                "model": ValidationErrorResponse
            }
        }
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )
    app.add_event_handler(
        "startup",
        execute_backend_server_event_handler(backend_app=app),
    )
    app.add_event_handler(
        "shutdown",
        terminate_backend_server_event_handler(backend_app=app),
    )
    app.add_exception_handler(
        RequestValidationError, validation_exception_handler
    )
    app.include_router(router=router, prefix=settings.API_PREFIX)
    app.openapi = lambda: custom_openapi(app)
    return app


backend_app: FastAPI = initialize_backend_application()
