import contextlib

from fastapi_users.exceptions import (
    InvalidPasswordException,
    UserAlreadyExists,
)

from cli.utils import print_error, print_success
from src.api.dependencies.repository import get_user_repository
from src.api.dependencies.session import get_async_session
from src.models.schemas.user import UserCreate

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_manager_context = contextlib.asynccontextmanager(get_user_repository)


async def create_user(email: str, password: str, is_superuser: bool = False):
    async with get_async_session_context() as session:
        async with get_user_manager_context(session) as user_manager:
            try:
                user = await user_manager.create(
                    UserCreate(
                        email=email,
                        password=password,
                        is_superuser=is_superuser,
                    )
                )
                print_success(
                    message=f"Пользователь [blue]{user.email}[/blue] создан"
                )
            except UserAlreadyExists:
                print_error(message="Такой пользователь уже существует")
            except InvalidPasswordException:
                print_error(
                    message="Проверьте пароль на соответствие правилам"
                )
