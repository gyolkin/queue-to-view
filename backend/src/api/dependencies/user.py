from fastapi import Depends
from fastapi_users import exceptions

from src.api.dependencies.repository import get_user_repository
from src.config.authentication import authenticator
from src.config.manager import settings
from src.models.db import User
from src.repository.crud import UserCRUDRepository
from src.utils.exceptions.http import http_exc_404_user_not_exists

current_user = authenticator.current_user(
    active=True, verified=settings.REGISTER_VERIFICATION
)
current_user_token = authenticator.current_user_token(
    active=True, verified=settings.REGISTER_VERIFICATION
)
current_superuser = authenticator.current_user(active=True, superuser=True)


async def get_user_or_404(
    id: str, user_manager: UserCRUDRepository = Depends(get_user_repository)
) -> User:
    """
    Зависимость для получения пользователя по id.

    params:
        id: Значение уникального идентификатора пользователя (UUID).
        user_manager: Объект UserCRUDRepository
    result:
        Объект пользователя User.
    """
    try:
        parsed_id = user_manager.parse_id(id)
        return await user_manager.get(parsed_id)
    except (exceptions.UserNotExists, exceptions.InvalidID):
        raise await http_exc_404_user_not_exists()
