from typing import Sequence

from fastapi import Depends

from src.api.dependencies.repository import get_repository
from src.models.db import Genre
from src.repository.crud import GenreCRUDRepository
from src.utils.exceptions.database import EntityNotExists
from src.utils.exceptions.http import http_exc_404_genre_not_exist


async def get_genre_or_404(
    genre_id: int,
    genre_repo: GenreCRUDRepository = Depends(
        get_repository(GenreCRUDRepository, Genre)
    ),
) -> Genre:
    """
    Зависимость для проверки существования жанра в БД (по id).

    params:
        genre_id: Значение уникального идентификатора жанра (ID).
        genre_repo: Объект GenreCRUDRepository.
    result:
        Объект Genre.
    exc:
        Вызывает HTTPException, если id жанра не найден в БД.
    """
    try:
        return await genre_repo.read_one(genre_id, by_field="id")
    except EntityNotExists as e:
        raise await http_exc_404_genre_not_exist(str(e))


async def get_genres_from_id_list_or_404(
    genres_id_list: list[int],
    genre_repo: GenreCRUDRepository = Depends(
        get_repository(GenreCRUDRepository, Genre)
    ),
) -> Sequence[Genre]:
    """
    Зависимость для проверки существования жанров в БД (по списку id).

    params:
        genres_id_list: Список значений уникальных идентификаторов жанра (ID).
        genre_repo: Объект GenreCRUDRepository.
    result:
        Список объектов Genre.
    exc:
        Вызывает HTTPException, если хотя бы один id не найден в БД.
    """
    genres = await genre_repo.read_by_id_list(genres_id_list)
    if len(genres) != len(genres_id_list):
        missing_ids = set(genres_id_list) - {genre.id for genre in genres}
        error_message = ", ".join(str(id) for id in missing_ids)
        raise await http_exc_404_genre_not_exist(error_message)
    return genres
