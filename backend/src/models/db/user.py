from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from src.repository.table import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
