from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)

from src.config.manager import settings


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_KEY, lifetime_seconds=settings.JWT_LIFETIME
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=CookieTransport(cookie_name="jwt_token"),
    get_strategy=get_jwt_strategy,
)
