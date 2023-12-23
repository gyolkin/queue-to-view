from fastapi import Depends
from fastapi_users import exceptions

from src.api.dependencies.repository import get_user_repository
from src.models.db import User
from src.repository.crud import UserCRUDRepository
from src.utils.exceptions.http import http_exc_404_user_not_exist


async def get_user_or_404(
    id: str, user_manager: UserCRUDRepository = Depends(get_user_repository)
) -> User:
    """
    Зависимость для проверки существования пользователя в БД (по id).

    params:
        id: Значение уникального идентификатора пользователя (UUID).
        user_manager: Объект UserCRUDRepository
    result:
        Объект User.
    """
    try:
        parsed_id = user_manager.parse_id(id)
        return await user_manager.get(parsed_id)
    except (exceptions.UserNotExists, exceptions.InvalidID):
        raise await http_exc_404_user_not_exist()
