from fastapi import APIRouter

from src.api.routes import (
    auth_router,
    genre_router,
    movie_router,
    user_router,
    watched_router,
)

router = APIRouter()
router.include_router(router=auth_router)
router.include_router(router=user_router)
router.include_router(router=movie_router)
router.include_router(router=watched_router)
router.include_router(router=genre_router)
