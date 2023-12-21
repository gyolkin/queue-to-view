from typing import Sequence

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.session import get_async_session
from src.models.db import Genre
from src.repository.crud import genre_repo
from src.utils.exceptions.database import EntityNotExists
from src.utils.exceptions.http import http_exc_404_genre_not_exist


async def get_genre_or_404(
    genre_id: int, session: AsyncSession = Depends(get_async_session)
) -> Genre:
    """ """
    try:
        return await genre_repo.read_one(
            session=session, value=genre_id, by_field="id"
        )
    except EntityNotExists as e:
        raise await http_exc_404_genre_not_exist(str(e))


async def get_genres_from_id_list_or_404(
    genres_id_list: list[int],
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[Genre]:
    """ """
    genres = await genre_repo.read_by_id_list(
        session=session, id_list=genres_id_list
    )
    if len(genres) != len(genres_id_list):
        missing_ids = set(genres_id_list) - {genre.id for genre in genres}
        error_message = ", ".join(str(id) for id in missing_ids)
        raise await http_exc_404_genre_not_exist(error_message)
    return genres
