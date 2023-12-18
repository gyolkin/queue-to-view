from typing import Optional

from fastapi import Depends

from src.api.dependencies.repository import get_repository
from src.api.dependencies.user import current_user_optional
from src.models.db import Movie, User
from src.repository.crud import MovieCRUDRepository
from src.utils.exceptions.database import EntityNotExists
from src.utils.exceptions.http import http_exc_404_movie_not_exist


async def get_movie_or_404(
    movie_slug: str,
    movie_repo: MovieCRUDRepository = Depends(
        get_repository(MovieCRUDRepository, Movie)
    ),
    user: Optional[User] = Depends(current_user_optional),
) -> Movie:
    """ """
    try:
        db_movie = await movie_repo.read_one(
            user=user, by_field="slug", value=movie_slug
        )
        return db_movie
    except EntityNotExists as e:
        raise await http_exc_404_movie_not_exist(str(e))


async def get_random_movie_or_404(
    movie_repo: MovieCRUDRepository = Depends(
        get_repository(MovieCRUDRepository, Movie)
    ),
    user: Optional[User] = Depends(current_user_optional),
) -> Movie:
    """ """
    random_movie = await movie_repo.read_one(user=user)
    return random_movie
