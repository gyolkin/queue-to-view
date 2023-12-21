from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession

from src.api.dependencies.session import get_async_session
from src.models.db import User
from src.repository.crud import UserCRUDRepository


def get_user_repository(
    async_session: SQLAlchemyAsyncSession = Depends(get_async_session),
) -> UserCRUDRepository:
    """
    Зависимость для получения репозитория пользовательской модели.

    Выделяется в отдельную функцию, поскольку зависит от third-party библиотеки FastAPI Users
    и существенно завязана на ее архитектуре.

    params:
        async_session: Асинхронная сессия SQLAlchemy, используемая для работы с базой данных.
    result:
        Экземпляр UserCRUDRepository, предоставляющий методы для CRUD-операций с пользователями.
    """
    user_db = SQLAlchemyUserDatabase(async_session, User)
    return UserCRUDRepository(user_db)
