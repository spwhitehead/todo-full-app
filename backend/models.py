from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLEnum

from pydantic import field_validator

from database import Base

from enum import Enum as PythonEnum

class Priority(PythonEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    DONOWORDIE = 4

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(1024))
    urgency = Column(Integer)

    #@field_validator("urgency", mode="before", check_fields=False)
    #def verify_int_in_urgency_enum(cls, value: int) -> int:
    #    for enum in Priority:
    #        if enum.value == value:
    #            return value
            
       # raise ValueError(f"Urgency value must be between 1 and 4. You entered {value}. Try again.")