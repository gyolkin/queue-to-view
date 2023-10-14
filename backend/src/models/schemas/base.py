from pydantic import BaseModel, ConfigDict


class BaseSchemaModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True, from_attributes=True, validate_assignment=True
    )
