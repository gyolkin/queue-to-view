from typing import Sequence

from sqlalchemy import select

from src.models.db.test import Test
from src.models.schemas.test import TestCreate
from src.repository.crud.base import BaseCRUDRepository


class TestCRUDRepository(BaseCRUDRepository):
    async def create_test(self, test_data: TestCreate) -> Test:
        new_test = Test(title=test_data.title)
        self.async_session.add(instance=new_test)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_test)
        return new_test

    async def read_tests(self) -> Sequence[Test]:
        query = await self.async_session.execute(statement=select(Test))
        return query.scalars().all()
