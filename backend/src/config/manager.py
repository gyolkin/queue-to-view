from functools import lru_cache

from src.config.constants import BackendConstants
from src.config.settings import BackendSettings


@lru_cache()
def get_settings() -> BackendSettings:
    return BackendSettings()


@lru_cache()
def get_constants() -> BackendConstants:
    return BackendConstants()


settings: BackendSettings = get_settings()
constants: BackendConstants = get_constants()
