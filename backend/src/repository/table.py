from typing import Type

from sqlalchemy import Integer, MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    mapped_column,
)


class CreateTableName:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class AutoincrementIDMixin:
    @declared_attr
    def id(cls):
        return mapped_column(Integer, primary_key=True)


class DBTable(DeclarativeBase, CreateTableName):
    metadata: MetaData = MetaData()


Base: Type[DeclarativeBase] = DBTable
