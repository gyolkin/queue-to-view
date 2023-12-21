from fastapi import APIRouter, Depends, Request, Response, status
from fastapi_users import exceptions, schemas

from src.api.dependencies.repository import get_user_repository
from src.api.dependencies.user import current_superuser, current_user
from src.api.shortcuts.user import get_user_or_404
from src.models.db import User
from src.models.schemas.exceptions import ErrorResponse
from src.models.schemas.user import UserRead, UserUpdate
from src.repository.crud import UserCRUDRepository
from src.utils.exceptions.http import (
    http_exc_400_invalid_password,
    http_exc_400_user_exists,
)

router = APIRouter(prefix="/user", tags=["user"])


@router.get(
    "/me",
    response_model=UserRead,
    summary="Получение информации о текущем пользователе",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorResponse,
            "description": "Пользователь не авторизован или деактивирован",
            "content": {
                "application/json": {
                    "example": {"detail": "Пользователь не авторизован"}
                }
            },
        },
    },
)
async def me(
    user: User = Depends(current_user),
):
    return schemas.model_validate(UserRead, user)


@router.patch(
    "/me",
    response_model=UserRead,
    dependencies=[Depends(current_user)],
    summary="Обновление информации о текущем пользователе",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorResponse,
            "description": "Пользователь не авторизован или деактивирован",
            "content": {
                "application/json": {
                    "example": {"detail": "Пользователь не авторизован"}
                }
            },
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse,
            "description": "Ошибка изменения данных пользователя",
            "content": {
                "application/json": {
                    "example": {"detail": "Некорректный пароль"}
                }
            },
        },
    },
)
async def update_me(
    request: Request,
    user_update: UserUpdate,
    user: User = Depends(current_user),
    user_manager: UserCRUDRepository = Depends(get_user_repository),
):
    try:
        user = await user_manager.update(
            user_update, user, safe=True, request=request
        )
        return schemas.model_validate(UserRead, user)
    except exceptions.UserAlreadyExists:
        raise await http_exc_400_user_exists()
    except exceptions.InvalidPasswordException as e:
        raise await http_exc_400_invalid_password(message=e.reason)


@router.get(
    "/{user_id}",
    response_model=UserRead,
    summary="Получение информации о пользователе по id",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse,
            "description": "Пользователь с таким id не найден в БД",
            "content": {
                "application/json": {
                    "example": {"detail": "Данный пользователь не найден"}
                }
            },
        },
    },
)
async def get_user(user: User = Depends(get_user_or_404)):
    return schemas.model_validate(UserRead, user)


@router.patch(
    "/{user_id}",
    response_model=UserRead,
    dependencies=[Depends(current_superuser)],
    summary="Обновление информации о пользователе по id (для админа)",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorResponse,
            "description": "Пользователь не авторизован или деактивирован",
            "content": {
                "application/json": {
                    "example": {"detail": "Пользователь не авторизован"}
                }
            },
        },
        status.HTTP_403_FORBIDDEN: {
            "model": ErrorResponse,
            "description": "Запрос на изменение не от админа",
            "content": {
                "application/json": {"example": {"detail": "Доступ запрещен"}}
            },
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse,
            "description": "Пользователь с таким id не найден в БД",
            "content": {
                "application/json": {
                    "example": {"detail": "Данный пользователь не найден"}
                }
            },
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse,
            "description": "Ошибка изменения данных пользователя",
            "content": {
                "application/json": {
                    "example": {"detail": "Некорректный пароль"}
                }
            },
        },
    },
)
async def update_user(
    user_update: UserUpdate,
    request: Request,
    user: User = Depends(get_user_or_404),
    user_manager: UserCRUDRepository = Depends(get_user_repository),
):
    try:
        user = await user_manager.update(
            user_update, user, safe=False, request=request
        )
    except exceptions.UserAlreadyExists:
        raise await http_exc_400_user_exists()
    except exceptions.InvalidPasswordException as e:
        raise await http_exc_400_invalid_password(message=e.reason)
    return schemas.model_validate(UserRead, user)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    dependencies=[Depends(current_superuser)],
    summary="Удаление пользователя из БД по id (для админа)",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorResponse,
            "description": "Пользователь не авторизован или деактивирован",
            "content": {
                "application/json": {
                    "example": {"detail": "Пользователь не авторизован"}
                }
            },
        },
        status.HTTP_403_FORBIDDEN: {
            "model": ErrorResponse,
            "description": "Запрос на изменение не от админа",
            "content": {
                "application/json": {"example": {"detail": "Доступ запрещен"}}
            },
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse,
            "description": "Пользователь с таким id не найден в БД",
            "content": {
                "application/json": {
                    "example": {"detail": "Данный пользователь не найден"}
                }
            },
        },
    },
)
async def delete_user(
    request: Request,
    user: User = Depends(get_user_or_404),
    user_manager: UserCRUDRepository = Depends(get_user_repository),
):
    await user_manager.delete(user, request=request)
    return None
