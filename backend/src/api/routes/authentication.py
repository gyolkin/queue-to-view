from fastapi import APIRouter, Depends, Request, status
from fastapi_users import exceptions, schemas

from src.api.dependencies.repository import get_user_repository
from src.api.dependencies.user import current_user_token
from src.config.authentication import AuthStrategy, UserToken, auth_backend
from src.config.manager import settings
from src.models.schemas.exceptions import ErrorResponse
from src.models.schemas.user import UserCreate, UserLogin, UserRead
from src.repository.crud.user import UserCRUDRepository
from src.utils.exceptions.http import (
    http_exc_400_invalid_credentials,
    http_exc_400_invalid_password,
    http_exc_400_not_verified,
    http_exc_400_user_exists,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Регистрация нового пользователя",
    responses={
        status.HTTP_201_CREATED: {"description": "Успешная регистрация"},
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse,
            "description": "Ошибка регистрации нового пользователя",
            "content": {
                "application/json": {
                    "example": {"detail": "Ошибка регистрации"}
                }
            },
        },
    },
)
async def register(
    request: Request,
    user_create: UserCreate,
    user_manager: UserCRUDRepository = Depends(get_user_repository),
):
    try:
        created_user = await user_manager.create(
            user_create, safe=True, request=request
        )
    except exceptions.UserAlreadyExists:
        raise await http_exc_400_user_exists()
    except exceptions.InvalidPasswordException as e:
        raise await http_exc_400_invalid_password(message=e.reason)
    return schemas.model_validate(UserRead, created_user)


@router.post(
    "/login",
    summary="Авторизация пользователя",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "model": None,
            "description": "Успешная авторизация",
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse,
            "description": "Ошибка авторизации",
            "content": {
                "application/json": {
                    "example": {"detail": "Ошибка авторизации"}
                }
            },
        },
    },
)
async def login(
    request: Request,
    user_login: UserLogin,
    user_manager: UserCRUDRepository = Depends(get_user_repository),
    strategy=Depends(auth_backend.get_strategy),
):
    user = await user_manager.authenticate(user_login)
    if user is None or not user.is_active:
        raise await http_exc_400_invalid_credentials()
    if settings.REGISTER_VERIFICATION and not user.is_verified:
        raise await http_exc_400_not_verified()
    response = await auth_backend.login(strategy, user)
    await user_manager.on_after_login(user, request, response)
    return response


@router.post(
    "/logout",
    summary="Выход из системы",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "model": None,
            "description": "Успешный выход",
        },
    },
)
async def logout(
    user_token: UserToken = Depends(current_user_token),
    strategy: AuthStrategy = Depends(auth_backend.get_strategy),
):
    user, token = user_token
    return await auth_backend.logout(strategy, user, token)
