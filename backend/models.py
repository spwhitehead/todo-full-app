from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLEnum

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
    urgency = Column(SQLEnum(Priority))