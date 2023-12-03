from fastapi import APIRouter, Depends

from src.api.dependencies.repository import get_repository
from src.api.shortcuts import get_country_or_404
from src.models.db import Country
from src.models.schemas.country import CountryRead
from src.repository.crud import CountryCRUDRepository

router = APIRouter(prefix="/country", tags=["country"])


@router.get(
    "",
    response_model=list[CountryRead],
    summary="Получение списка всех стран",
)
async def get_countries(
    country_repo: CountryCRUDRepository = Depends(
        get_repository(CountryCRUDRepository, Country)
    ),
):
    db_countries = await country_repo.read_all()
    return db_countries


@router.get(
    "/{country_id}",
    response_model=CountryRead,
    summary="Получение конкретной страны по id",
)
async def get_country(db_country: Country = Depends(get_country_or_404)):
    return db_country
