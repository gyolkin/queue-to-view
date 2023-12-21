from typing import Generic, Sequence, Type, TypeVar

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
    def __init__(self, model: Type[DBModelType]):
        self.model = model

    async def create(
        self, session: AsyncSession, input_object: CreateSchemaType
    ) -> DBModelType:
        db_object = self.model(**input_object.model_dump())
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def read_all(self, session: AsyncSession) -> Sequence[DBModelType]:
        stmt = sqlalchemy.select(self.model)
        query = await session.execute(statement=stmt)
        return query.scalars().all()

    async def read_one(
        self,
        session: AsyncSession,
        value: str | int,
        by_field: str = "id",
    ) -> DBModelType:
        stmt = sqlalchemy.select(self.model).filter(
            getattr(self.model, by_field) == value
        )
        query = await session.execute(statement=stmt)
        result = query.unique().scalar_one_or_none()

        if result is None:
            raise EntityNotExists(value)

        return result

    async def update(
        self,
        session: AsyncSession,
        db_object: DBModelType,
        input_object: UpdateSchemaType,
    ) -> DBModelType:
        current_data = encoders.jsonable_encoder(db_object)
        update_data = input_object.model_dump(exclude_unset=True)
        for field in current_data:
            if field in update_data:
                setattr(db_object, field, update_data[field])
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def delete(
        self, session: AsyncSession, db_object: DBModelType
    ) -> None:
        await session.delete(db_object)
        await session.commit()
        return None
