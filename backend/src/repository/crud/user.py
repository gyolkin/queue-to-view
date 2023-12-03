import uuid
from typing import Optional, Union

from fastapi_users import (
    BaseUserManager,
    InvalidPasswordException,
    UUIDIDMixin,
    exceptions,
)

from src.config.manager import settings
from src.models.db import User
from src.models.schemas.user import UserCreate, UserLogin


class UserCRUDRepository(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    async def authenticate(self, user_login: UserLogin) -> Optional[User]:
        try:
            user = await self.get_by_email(user_login.email)
        except exceptions.UserNotExists:
            self.password_helper.hash(user_login.password)
            return None
        (
            verified,
            updated_password_hash,
        ) = self.password_helper.verify_and_update(
            user_login.password, user.hashed_password
        )
        if not verified:
            return None
        if updated_password_hash is not None:
            await self.user_db.update(
                user, {"hashed_password": updated_password_hash}
            )
        return user

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < settings.PASSWORD_MIN_LENGTH:
            raise InvalidPasswordException(
                reason=f"пароль должен быть длиннее {settings.PASSWORD_MIN_LENGTH} символов"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="пароль не должен содержать в себе имя пользователя"
            )
