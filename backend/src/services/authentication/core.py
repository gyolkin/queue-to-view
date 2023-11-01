import uuid

from fastapi_users import FastAPIUsers

from src.models.db import User
from src.services.authentication import auth_backend
from src.services.authentication.manager import get_user_manager

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
