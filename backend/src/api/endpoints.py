import fastapi

from src.api.routes import main_router

router = fastapi.APIRouter(prefix="/api")

router.include_router(router=main_router)
