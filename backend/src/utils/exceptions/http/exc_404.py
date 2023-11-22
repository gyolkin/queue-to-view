from fastapi import HTTPException, status

from src.utils.messages.exceptions import http_404_user_not_exists_details


async def http_exc_404_user_not_exists() -> Exception:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=http_404_user_not_exists_details(),
    )
