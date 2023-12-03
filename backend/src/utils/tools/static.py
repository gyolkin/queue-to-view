import base64
import uuid

import aiofiles

from src.config.manager import settings


async def create_image_from_bytes(content: bytes) -> str:
    """
    Функция для декодирования base64 в изображение.
    Сохраняет результат в формате .jpg на диске.

    params:
        content: Строка base64.
    result:
        Строковое название созданной картинки.
    """
    image_name = f"{uuid.uuid4()}.jpg"
    image_decoded = base64.b64decode(content)
    file_path = f"{settings.get_static_folder_path}/{image_name}"
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(image_decoded)
    return image_name
