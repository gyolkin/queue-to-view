from functools import lru_cache

from src.config.settings import BackendSettings


@lru_cache()
def get_settings() -> BackendSettings:
    return BackendSettings()


settings: BackendSettings = get_settings()
