from src.models.schemas.base import BaseSchemaModel


class TestCreate(BaseSchemaModel):
    title: str


class TestResponse(BaseSchemaModel):
    id: int
    title: str
