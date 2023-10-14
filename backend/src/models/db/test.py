from sqlalchemy.orm import Mapped, mapped_column

from src.repository.table import Base


class Test(Base):
    __tablename__ = "test_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    title: Mapped[str] = mapped_column()

    __mapper_args__ = {"eager_defaults": True}
