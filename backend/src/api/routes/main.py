from fastapi import APIRouter

router = APIRouter(prefix="/main", tags=["main"])


@router.get(
    "/",
)
async def hello_world():
    """
    Пример базового эндпоинта.
    """
    return {"hello": "world!"}
