from src.models.db import Country
from src.models.schemas.country import CountryCreate, CountryUpdate
from src.repository.crud.base import BaseCRUDRepository


class CountryCRUDRepository(
    BaseCRUDRepository[Country, CountryCreate, CountryUpdate]
):
    pass
