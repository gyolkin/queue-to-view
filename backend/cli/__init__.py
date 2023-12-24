import asyncio
from typing import Annotated

from typer import Option, Typer

from cli.commands import create_user, movie_import

console_app = Typer()


@console_app.command()
def createuser(
    email: Annotated[str, Option(prompt="Имя пользователя (Email)")],
    password: Annotated[str, Option(prompt="Пароль", hide_input=True)],
    is_superuser: Annotated[
        bool, Option(prompt="Выдать права администратора?")
    ],
):
    """Создание нового пользователя."""
    asyncio.run(create_user(email, password, is_superuser))


@console_app.command()
def movieimport(
    filename: Annotated[
        str,
        Option(..., "-f", "--filename", help="Путь к .json файлу с фильмами"),
    ],
    email: Annotated[
        str,
        Option(
            prompt="Имя пользователя (Email)",
            help="Email пользователя для авторизации",
        ),
    ],
    password: Annotated[
        str,
        Option(
            prompt="Пароль",
            hide_input=True,
            help="Пароль пользователя для авторизации",
        ),
    ],
):
    """Массовое добавление фильмов из JSON файла (требует авторизации)"""
    asyncio.run(movie_import(filename, email, password))
