from dataclasses import dataclass


@dataclass(frozen=True)
class BackendConstants:
    MAX_TITLE_LENGTH: int = 256
    MAX_SLUG_LENGTH: int = 512
    MAX_TEXT_LENGTH: int = 1024

    MIN_RELEASE_YEAR: int = 1900
    MAX_RELEASE_YEAR: int = 2030
