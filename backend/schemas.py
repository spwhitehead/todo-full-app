import json
from pydantic import BaseModel, field_validator
from sqlalchemy.types import Enum as SQLEnum
from enum import Enum as PythonEnum


class Priority(PythonEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    DONOWORDIE = 4


class TodoBase(BaseModel):
    title: str
    description: str
    urgency: int

    @field_validator("urgency", mode="before", check_fields=False)
    def verify_int_in_urgency_enum(cls, value: int) -> int:
        for enum in Priority:
            if enum.value == value:
                return value
            
        raise ValueError(f"Urgency value must be between 1 and 4. You entered {value}. Try again.")


class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id : int

    class Config:
        from_attributes = True