import uuid
from typing import Tuple

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    Authenticator,
    CookieTransport,
    JWTStrategy,
    Strategy,
)

from src.api.dependencies.repository import get_user_repository
from src.config.manager import settings
from src.models.db import User


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_KEY, lifetime_seconds=settings.JWT_LIFETIME
    )


cookie_transport = CookieTransport(
    cookie_name=settings.AUTH_COOKIE_NAME, cookie_max_age=settings.JWT_LIFETIME
)
jwt_strategy = get_jwt_strategy

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_repository,
    [auth_backend],
)

UserToken = Tuple[User, str]
AuthStrategy = Strategy[User, uuid.UUID]

authenticator = Authenticator([auth_backend], get_user_repository)
