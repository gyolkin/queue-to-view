from typing import Dict, List

from pydantic import BaseModel


class ValidationErrorResponse(BaseModel):
    detail: Dict[str, List[str]]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "field_1": ["Validation Error"],
                    "field_2": ["Validation Error"],
                }
            ]
        }
    }


class ErrorResponse(BaseModel):
    detail: str
