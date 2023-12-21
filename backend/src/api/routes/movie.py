from typing import Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.session import get_async_session
from src.api.dependencies.user import current_superuser, current_user_optional
from src.api.shortcuts import (
    get_genres_from_id_list_or_404,
    get_movie_or_404,
    get_random_movie_or_404,
)
from src.models.db import Movie, User
from src.models.schemas.movie import (
    MovieCreate,
    MovieDetailedRead,
    MovieUpdate,
)
from src.repository.crud import movie_repo
from src.utils.docs import create_movie_details

router = APIRouter(prefix="/movie", tags=["movie"])


@router.get(
    "",
    response_model=list[MovieDetailedRead],
    summary="Получение списка всех фильмов",
    openapi_extra={"security": None},
)
async def get_movies(
    hide_watched: bool = False,
    session: AsyncSession = Depends(get_async_session),
    user: Optional[User] = Depends(current_user_optional),
):
    db_movies = await movie_repo.read_all(
        session=session,
        user_id=user.id if user else None,
        hide_watched=hide_watched
    )
    return db_movies


@router.get(
    "/random-movie",
    response_model=MovieDetailedRead,
    summary="Получение случайного фильма из базы данных",
    openapi_extra={"security": None},
)
async def get_random_movie(
    random_movie: Movie = Depends(get_random_movie_or_404),
):
    return random_movie


@router.get(
    "/{movie_slug}",
    response_model=MovieDetailedRead,
    summary="Получение конкретного фильма по slug",
    openapi_extra={"security": None},
)
async def get_movie(db_movie: Movie = Depends(get_movie_or_404)):
    return db_movie


@router.post(
    "",
    response_model=MovieDetailedRead,
    summary="Добавление нового фильма",
    dependencies=[Depends(current_superuser)],
    responses=create_movie_details,
)
async def create_movie(
    movie_create: MovieCreate,
    session: AsyncSession = Depends(get_async_session),
):
    genres = await get_genres_from_id_list_or_404(
        session=session, genres_id_list=movie_create.genres
    )
    new_movie = await movie_repo.create(
        session=session, input_object=movie_create, genres=genres
    )
    return new_movie


@router.patch(
    "/{movie_slug}",
    response_model=MovieDetailedRead,
    summary="Изменение существующего фильма по slug",
    responses=create_movie_details,
)
async def update_movie(
    movie_update: MovieUpdate,
    session: AsyncSession = Depends(get_async_session),
    db_movie: Movie = Depends(get_movie_or_404),
):
    genres = (
        await get_genres_from_id_list_or_404(
            session=session, genres_id_list=movie_update.genres
        )
        if movie_update.genres
        else None
    )
    updated_movie = await movie_repo.update(
        session=session,
        db_object=db_movie,
        input_object=movie_update,
        genres=genres,
    )
    return updated_movie


@router.delete(
    "/{movie_slug}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(current_superuser)],
    summary="Удаление фильма из БД по slug",
)
async def delete_movie(
    session: AsyncSession = Depends(get_async_session),
    db_movie: Movie = Depends(get_movie_or_404),
):
    await movie_repo.delete(session=session, db_object=db_movie)
    return None
