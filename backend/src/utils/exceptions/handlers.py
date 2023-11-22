from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    errors = exc.errors()
    formatted_errors = {}
    for error in errors:
        field = error["loc"][1]
        msg = error["msg"]
        if field not in formatted_errors:
            formatted_errors[field] = []
        formatted_errors[field].append(msg)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": formatted_errors},
    )
