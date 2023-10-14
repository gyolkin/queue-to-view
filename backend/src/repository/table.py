from typing import Type

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


class DBTable(DeclarativeBase):
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()


Base: Type[DeclarativeBase] = DBTable
