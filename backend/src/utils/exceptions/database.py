class EntityNotExists(Exception):
    """
    Такая запись не существует в БД.
    """


class EntityAlreadyExists(Exception):
    """
    Такая запись уже существует в БД.
    """
