import uuid

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)

from src.config.manager import settings
from src.models.db import User
from src.repository.user import get_user_manager


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_KEY, lifetime_seconds=settings.JWT_LIFETIME
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=CookieTransport(cookie_name="jwt_token"),
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
