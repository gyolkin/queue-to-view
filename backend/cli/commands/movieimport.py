import contextlib
import json

from httpx import AsyncClient, Cookies
from rich import progress

from cli.constants import BASE_BACKEND_URL, GENRES
from cli.utils import (
    print_error,
    print_success,
    print_success_finish,
    print_warning,
)
from src.api.dependencies.session import get_async_session
from src.models.schemas.genre import GenreCreate
from src.repository.crud import genre_repo

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
cookies = Cookies()


async def movie_import(filename: str, email: str, password: str):
    try:
        with open(filename, "r") as file:
            movies = json.load(file)
    except FileNotFoundError:
        print_error(message="Файл не найден")
        return
    except json.JSONDecodeError:
        print_error(message="Ошибка в формате JSON")
        return

    async with AsyncClient() as client:
        response = await client.post(
            BASE_BACKEND_URL + "/auth/login",
            json={"email": email, "password": password},
        )
        token = response.cookies.get("jwt_token")
        if not token:
            print_error(message="Проверьте учетные данные")
            return
        cookies.set("jwt_token", token)
        print_success(message="Вы авторизовались")

        genre_response = await client.get(BASE_BACKEND_URL + "/genre")
        if not genre_response.json():
            print_warning(
                message="В базе данных нет жанров. Сейчас они будут автоматически добавлены"
            )
            async with get_async_session_context() as session:
                for genre in progress.track(
                    GENRES, description="Добавляем жанры..."
                ):
                    genre = await genre_repo.create(
                        session=session,
                        input_object=GenreCreate(
                            title=genre[0], slug=genre[1]
                        ),
                    )
            print_success_finish(message="Жанры добавлены в базу данных")

        success_counter = 0
        for movie in progress.track(movies, description="Добавляем фильмы..."):
            response = await client.post(
                BASE_BACKEND_URL + "/movie", cookies=cookies, json=movie
            )
            if response.status_code == 403:
                print_error(
                    message="Проверьте, что вы авторизовались как администратор"
                )
                return
            if response.status_code == 200:
                success_counter += 1
    print_success_finish(message=f"Было добавлено {success_counter} фильмов")
