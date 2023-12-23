from fastapi import APIRouter, Depends

from src.api.dependencies.repository import get_repository
from src.api.shortcuts import get_genre_or_404
from src.models.db import Genre
from src.models.schemas.genre import GenreRead
from src.repository.crud import GenreCRUDRepository

router = APIRouter(prefix="/genre", tags=["genre"])


@router.get(
    "",
    response_model=list[GenreRead],
    summary="Получение списка всех жанров",
)
async def get_genres(
    genre_repo: GenreCRUDRepository = Depends(
        get_repository(GenreCRUDRepository, Genre)
    ),
):
    db_genres = await genre_repo.read_all()
    return db_genres


@router.get(
    "/{genre_id}",
    response_model=GenreRead,
    summary="Получение конкретного жанра по id",
)
async def get_genre(db_genre: Genre = Depends(get_genre_or_404)):
    return db_genre
