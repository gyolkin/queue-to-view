from fastapi import APIRouter

from src.api.routes import user_router

router = APIRouter()
router.include_router(router=user_router)
