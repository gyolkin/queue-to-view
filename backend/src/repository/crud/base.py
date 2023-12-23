from typing import Generic, Optional, Sequence, Type, TypeVar

import sqlalchemy
from fastapi import encoders
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.schemas.base import BaseSchemaModel
from src.repository.table import Base
from src.utils.exceptions.database import EntityNotExists

DBModelType = TypeVar("DBModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseSchemaModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseSchemaModel)


class BaseCRUDRepository(
    Generic[DBModelType, CreateSchemaType, UpdateSchemaType]
):
    def __init__(self, async_session: AsyncSession, model: Type[DBModelType]):
        self.async_session = async_session
        self.model = model

    async def create(self, input_object: CreateSchemaType) -> DBModelType:
        db_object = self.model(**input_object.model_dump())
        self.async_session.add(db_object)
        await self.async_session.commit()
        await self.async_session.refresh(db_object)
        return db_object

    async def read_all(self) -> Sequence[DBModelType]:
        stmt = sqlalchemy.select(self.model)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def read_one(
        self,
        value: str | int,
        by_field: str = "id",
    ) -> DBModelType:
        stmt = sqlalchemy.select(self.model).filter(
            getattr(self.model, by_field) == value
        )
        query = await self._read(statement=stmt)
        if query is None:
            raise EntityNotExists(value)
        return query

    async def update(
        self, db_object: DBModelType, input_object: UpdateSchemaType
    ) -> DBModelType:
        current_data = encoders.jsonable_encoder(db_object)
        update_data = input_object.model_dump(exclude_unset=True)
        for field in current_data:
            if field in update_data:
                setattr(db_object, field, update_data[field])
        self.async_session.add(db_object)
        await self.async_session.commit()
        await self.async_session.refresh(db_object)
        return db_object

    async def delete(self, db_object: DBModelType) -> None:
        await self.async_session.delete(db_object)
        await self.async_session.commit()
        return None

    async def _read(
        self, statement: sqlalchemy.Select
    ) -> Optional[DBModelType]:
        query = await self.async_session.execute(statement)
        return query.unique().scalar_one_or_none()
