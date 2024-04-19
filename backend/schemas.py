from pydantic import BaseModel
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
    urgency: Priority

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id : int

    class Config:
        from_attributes = True