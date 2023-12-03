from fastapi import HTTPException, status

from src.utils.messages.exceptions import (
    http_404_country_not_exist_details,
    http_404_genre_not_exist_details,
    http_404_movie_not_exist_details,
    http_404_user_not_exist_details,
)


async def http_exc_404_user_not_exist() -> Exception:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=http_404_user_not_exist_details(),
    )


async def http_exc_404_country_not_exist(message: str | int) -> Exception:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=http_404_country_not_exist_details(message),
    )


async def http_exc_404_movie_not_exist(message: str | int) -> Exception:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=http_404_movie_not_exist_details(message),
    )


async def http_exc_404_genre_not_exist(message: str | int) -> Exception:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=http_404_genre_not_exist_details(message),
    )
