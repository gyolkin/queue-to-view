from fastapi import APIRouter

from src.api.routes import auth_router, user_router

router = APIRouter()
router.include_router(router=auth_router)
router.include_router(router=user_router)
