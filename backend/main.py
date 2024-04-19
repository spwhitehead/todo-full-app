from fastapi import FastAPI

import models
import schemas

from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

todos: list[schemas.Todo] = []


@app.get("/")
async def get_todos() -> list[schemas.Todo]:
    return todos


@app.post("/")
async def create_todo(todo: schemas.Todo) -> None:
    todos.append(todo)