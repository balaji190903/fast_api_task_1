from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Fast api task 1 is running succesfully ."}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks", status_code=201)
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):

    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task Added Successfully",
        "task": new_task
    }


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):

    tasks = db.query(models.Task).all()

    return tasks


@app.put("/tasks/{id}")
def update_task(
    id: int,
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):

    update = db.query(models.Task).filter(models.Task.id == id).first()

    if not update:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    update.title = task.title
    update.description = task.description
    update.status = task.status

    db.commit()
    db.refresh(update)

    return {
        "message": "Task Updated Successfully",
        "task": update
    }



@app.delete("/tasks/{id}")
def delete_task(
    id: int,
    db: Session = Depends(get_db)
):

    task = db.query(models.Task).filter(models.Task.id == id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task Deleted Successfully"
    }