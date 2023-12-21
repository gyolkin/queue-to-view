from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.session import get_async_session
from src.api.dependencies.user import current_user
from src.api.shortcuts import get_movie_or_404
from src.models.db import Movie, User
from src.repository.crud import watched_repo
from src.utils.exceptions.http import (
    http_exc_400_already_added_to_watchlist,
    http_exc_400_not_added_to_watchlist,
)

router = APIRouter(prefix="/movie", tags=["watchlist"])


@router.post(
    "/{movie_slug}/watch",
    status_code=status.HTTP_201_CREATED,
    summary="Добавление фильма в список просмотренных",
)
async def add_to_watchlist(
    session: AsyncSession = Depends(get_async_session),
    db_movie: Movie = Depends(get_movie_or_404),
    user: User = Depends(current_user),
):
    is_watched = await watched_repo.read_by_movie_id(
        session=session, user_id=user.id, movie_id=db_movie.id
    )
    if is_watched:
        raise await http_exc_400_already_added_to_watchlist()
    await watched_repo.create(
        session=session, user_id=user.id, movie_id=db_movie.id
    )
    return None


@router.delete(
    "/{movie_slug}/unwatch",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удаление фильма из списка просмотренных",
)
async def delete_from_watchlist(
    session: AsyncSession = Depends(get_async_session),
    db_movie: Movie = Depends(get_movie_or_404),
    user: User = Depends(current_user),
):
    is_watched = await watched_repo.read_by_movie_id(
        session=session, user_id=user.id, movie_id=db_movie.id
    )
    if not is_watched:
        raise await http_exc_400_not_added_to_watchlist()
    await watched_repo.delete(session=session, db_object=is_watched)
    return None
