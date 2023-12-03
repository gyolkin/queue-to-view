from fastapi import Depends

from src.api.dependencies.repository import get_repository
from src.models.db import Movie
from src.repository.crud import MovieCRUDRepository
from src.utils.exceptions.database import EntityNotExists
from src.utils.exceptions.http import http_exc_404_movie_not_exist


async def get_movie_or_404(
    movie_slug: str,
    movie_repo: MovieCRUDRepository = Depends(
        get_repository(MovieCRUDRepository, Movie)
    ),
) -> Movie:
    """
    Зависимость для проверки существования фильма в БД (по slug).

    params:
        movie_slug: Значение уникального идентификатора фильма (slug).
        movie_repo: Объект MovieCRUDRepository
    result:
        Объект Movie.
    exc:
        Вызывает HTTPException, если slug фильма не найден в БД.
    """
    try:
        return await movie_repo.read_one(movie_slug, by_field="slug")
    except EntityNotExists as e:
        raise await http_exc_404_movie_not_exist(str(e))
