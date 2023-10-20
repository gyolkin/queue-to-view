from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR: Path = Path(__file__).parent.parent.parent.parent.resolve()


class BackendSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{ROOT_DIR}/.env", case_sensitive=True
    )

    # APPLICATION
    INCLUDE_PARSER: bool = False
    TITLE: str = "Default Title"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "No description."
    DEBUG: bool = True
    DOCS_URL: str = "/docs"
    API_PREFIX: str = "/api"

    # DATABASE
    POSTGRES_DB: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_SCHEMA: str = "postgresql"
    POSTGRES_USERNAME: str = "postgres"
    POSTGRES_HOST: str = "db"

    # CORS
    IS_ALLOWED_CREDENTIALS: bool = True
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:80",
    ]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]

    @property
    def set_backend_app_attributes(self) -> dict[str, Optional[str | bool]]:
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "api_prefix": self.API_PREFIX,
        }
