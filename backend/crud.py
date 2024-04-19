from sqlalchemy.orm import Session

import models
import schemas

def get_todos(db: Session):
    return db.query(models.Todo).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.model_dump())
   # db_todo = models.Todo(title=todo.title, description=todo.description, urgency=todo.urgency.name)
   # db_todo = models.Todo(**todo.model_dump(), urgency=todo.urgency.name)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo