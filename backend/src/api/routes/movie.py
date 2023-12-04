from fastapi import APIRouter, Depends, status

from src.api.dependencies.repository import get_repository
from src.api.dependencies.user import current_superuser
from src.api.shortcuts import get_genres_from_id_list_or_404, get_movie_or_404
from src.models.db import Genre, Movie
from src.models.schemas.movie import (
    MovieCreate,
    MovieDetailedRead,
    MovieUpdate,
)
from src.repository.crud import GenreCRUDRepository, MovieCRUDRepository
from src.utils.docs import create_movie_details

router = APIRouter(prefix="/movie", tags=["movie"])


@router.get(
    "",
    response_model=list[MovieDetailedRead],
    summary="Получение списка всех фильмов",
)
async def get_movies(
    movie_repo: MovieCRUDRepository = Depends(
        get_repository(MovieCRUDRepository, Movie)
    ),
):
    db_movies = await movie_repo.read_all()
    return db_movies


@router.post(
    "",
    response_model=MovieDetailedRead,
    summary="Добавление нового фильма",
    dependencies=[Depends(current_superuser)],
    responses=create_movie_details,
)
async def create_movie(
    movie_create: MovieCreate,
    movie_repo: MovieCRUDRepository = Depends(
        get_repository(MovieCRUDRepository, Movie)
    ),
    genre_repo: GenreCRUDRepository = Depends(
        get_repository(GenreCRUDRepository, Genre)
    ),
):
    genres = await get_genres_from_id_list_or_404(
        movie_create.genres, genre_repo
    )
    new_movie = await movie_repo.create(movie_create, genres)
    return new_movie


@router.get(
    "/{movie_slug}",
    response_model=MovieDetailedRead,
    summary="Получение конкретного фильма по slug",
)
async def get_movie(db_movie: Movie = Depends(get_movie_or_404)):
    return db_movie


@router.patch(
    "/{movie_slug}",
    response_model=MovieDetailedRead,
    summary="Изменение существующего фильма по slug",
    dependencies=[Depends(current_superuser)],
    responses=create_movie_details,
)
async def update_movie(
    movie_update: MovieUpdate,
    db_movie: Movie = Depends(get_movie_or_404),
    movie_repo: MovieCRUDRepository = Depends(
        get_repository(MovieCRUDRepository, Movie)
    ),
    genre_repo: GenreCRUDRepository = Depends(
        get_repository(GenreCRUDRepository, Genre)
    ),
):
    genres = (
        await get_genres_from_id_list_or_404(movie_update.genres, genre_repo)
        if movie_update.genres
        else None
    )
    updated_movie = await movie_repo.update(db_movie, movie_update, genres)
    return updated_movie


@router.delete(
    "/{movie_slug}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удаление фильма из БД по slug",
    dependencies=[Depends(current_superuser)],
)
async def delete_movie(
    db_movie: Movie = Depends(get_movie_or_404),
    movie_repo: MovieCRUDRepository = Depends(
        get_repository(MovieCRUDRepository, Movie)
    ),
):
    await movie_repo.delete(db_movie)
    return None
