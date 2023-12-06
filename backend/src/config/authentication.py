import uuid
from typing import Tuple

from fastapi import Response
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


class CustomCookieTransport(CookieTransport):
    def __init__(
        self, *args, additional_cookie_name: str = "logged_in", **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.additional_cookie_name = additional_cookie_name

    async def get_login_response(self, token: str) -> Response:
        response = await super().get_login_response(token)
        if self.cookie_httponly:
            response.set_cookie(
                self.additional_cookie_name,
                "true",
                max_age=self.cookie_max_age,
                path=self.cookie_path,
                domain=self.cookie_domain,
                secure=self.cookie_secure,
            )
        return response

    async def get_logout_response(self) -> Response:
        response = await super().get_logout_response()
        if self.cookie_httponly:
            response.set_cookie(
                self.additional_cookie_name,
                "",
                max_age=0,
                path=self.cookie_path,
                domain=self.cookie_domain,
                secure=self.cookie_secure,
            )
        return response


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_KEY, lifetime_seconds=settings.JWT_LIFETIME
    )


cookie_transport = CustomCookieTransport(
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
