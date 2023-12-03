from typing import Any


def normalize_str(value: str) -> str:
    if not value.strip():
        raise ValueError("Значение поля не может быть пустым.")
    return value.strip()


def check_list_not_empty(seq: list[Any]) -> list[Any]:
    if not len(seq):
        raise ValueError("Список не может быть пустым.")
    return seq
