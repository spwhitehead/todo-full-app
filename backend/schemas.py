from pydantic import BaseModel
from enum import Enum


class Priority(Enum):
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
        orm_mode = True