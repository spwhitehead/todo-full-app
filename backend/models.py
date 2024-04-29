from sqlalchemy import Column, Integer, String

from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(1024))
    urgency = Column(Integer)