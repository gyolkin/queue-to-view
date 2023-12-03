from typing import Any, Dict, Optional

from fastapi import status

from src.models.schemas.exceptions import ErrorResponse
from src.utils.messages.exceptions import http_404_country_not_exist_details

OpenAPIType = Optional[Dict[int | str, Dict[str, Any]]]

create_movie_details: OpenAPIType = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Указанный id страны не существует в базе данных",
        "content": {
            "application/json": {
                "example": {"detail": http_404_country_not_exist_details()}
            }
        },
    },
}
