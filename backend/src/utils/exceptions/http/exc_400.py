from fastapi import HTTPException, status

from src.utils.messages.exceptions import (
    http_400_invalid_credentials_details,
    http_400_invalid_password_details,
    http_400_not_verified_details,
    http_400_user_exists_details,
)


async def http_exc_400_user_exists() -> Exception:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=http_400_user_exists_details(),
    )


async def http_exc_400_invalid_password(message: str) -> Exception:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=http_400_invalid_password_details(message),
    )


async def http_exc_400_invalid_credentials() -> Exception:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=http_400_invalid_credentials_details(),
    )


async def http_exc_400_not_verified() -> Exception:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=http_400_not_verified_details(),
    )
