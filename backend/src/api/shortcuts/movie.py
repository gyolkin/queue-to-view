from typing import Optional

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.session import get_async_session
from src.api.dependencies.user import current_user_optional
from src.models.db import Movie, User
from src.repository.crud import movie_repo
from src.utils.exceptions.database import EntityNotExists
from src.utils.exceptions.http import http_exc_404_movie_not_exist


async def get_movie_or_404(
    movie_slug: str,
    session: AsyncSession = Depends(get_async_session),
    user: Optional[User] = Depends(current_user_optional),
) -> Movie:
    """ """
    try:
        db_movie = await movie_repo.read_one(
            session=session,
            by_field="slug",
            value=movie_slug,
            user_id=user.id if user else None,
        )
        return db_movie
    except EntityNotExists as e:
        raise await http_exc_404_movie_not_exist(str(e))


async def get_random_movie_or_404(
    session: AsyncSession = Depends(get_async_session),
    user: Optional[User] = Depends(current_user_optional),
) -> Movie:
    """ """
    random_movie = await movie_repo.read_one(
        session=session, user_id=user.id if user else None
    )
    return random_movie
