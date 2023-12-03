from fastapi import Depends

from src.api.dependencies.repository import get_repository
from src.models.db import Country
from src.repository.crud import CountryCRUDRepository
from src.utils.exceptions.database import EntityNotExists
from src.utils.exceptions.http import http_exc_404_country_not_exist


async def get_country_or_404(
    country_id: int,
    country_repo: CountryCRUDRepository = Depends(
        get_repository(CountryCRUDRepository, Country)
    ),
) -> Country:
    """
    Зависимость для проверки существования страны в БД (по id).

    params:
        country_id: Значение уникального идентификатора страны (ID).
        country_repo: Объект CountryCRUDRepository
    result:
        Объект Country.
    exc:
        Вызывает HTTPException, если id страны не найден в БД.
    """
    try:
        return await country_repo.read_one(country_id, by_field="id")
    except EntityNotExists as e:
        raise await http_exc_404_country_not_exist(str(e))
