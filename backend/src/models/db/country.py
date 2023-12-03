from sqlalchemy import String
from sqlalchemy.orm import mapped_column, relationship

from src.config.manager import constants
from src.repository.table import AutoincrementIDMixin, Base


class Country(Base, AutoincrementIDMixin):
    title = mapped_column(String(constants.MAX_TITLE_LENGTH), nullable=False)
    slug = mapped_column(
        String(constants.MAX_SLUG_LENGTH), unique=True, nullable=False
    )

    movie = relationship("Movie", back_populates="country")
