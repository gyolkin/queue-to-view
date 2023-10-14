from fastapi import APIRouter

from src.api.routes import test_router

router = APIRouter()
router.include_router(router=test_router)
