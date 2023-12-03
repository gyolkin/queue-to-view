from typing import Any, Dict

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def custom_openapi(backend_app: FastAPI) -> Dict[str, Any]:
    if backend_app.openapi_schema:
        return backend_app.openapi_schema
    openapi_schema = get_openapi(
        title=backend_app.title,
        description=backend_app.description,
        version=backend_app.version,
        routes=backend_app.routes,
    )
    for method in openapi_schema["paths"]:
        for m in ("get", "delete"):
            try:
                del openapi_schema["paths"][method][m]["responses"]["422"]
            except KeyError:
                pass
    for schema in list(openapi_schema["components"]["schemas"]):
        if schema == "HTTPValidationError" or schema == "ValidationError":
            del openapi_schema["components"]["schemas"][schema]
    backend_app.openapi_schema = openapi_schema
    return backend_app.openapi_schema
