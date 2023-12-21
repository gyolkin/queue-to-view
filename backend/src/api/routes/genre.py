from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.session import get_async_session
from src.api.shortcuts import get_genre_or_404
from src.models.db import Genre
from src.models.schemas.genre import GenreRead
from src.repository.crud import genre_repo

router = APIRouter(prefix="/genre", tags=["genre"])


@router.get(
    "",
    response_model=list[GenreRead],
    summary="Получение списка всех жанров",
)
async def get_genres(
    session: AsyncSession = Depends(get_async_session),
):
    db_genres = await genre_repo.read_all(session=session)
    return db_genres


@router.get(
    "/{genre_id}",
    response_model=GenreRead,
    summary="Получение конкретного жанра по id",
)
async def get_genre(db_genre: Genre = Depends(get_genre_or_404)):
    return db_genre
