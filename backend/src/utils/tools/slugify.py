import uuid

from slugify import slugify


def generate_slug(title: str, include_uuid: bool) -> str:
    """
    Функция для преобразования названия ресурса в человекочитаемый slug.

    params:
        title: Строковое название ресурса.
        include_uuid: Дополнительно устанавливает 8-значный
            случайный код в конец ссылки.
    result:
        Строковый человекочитаемый slug.
    """
    base_slug = slugify(title, max_length=50)
    if include_uuid:
        unique_identifier = str(uuid.uuid4())[:8]
        return f"{base_slug}-{unique_identifier}"
    return base_slug
