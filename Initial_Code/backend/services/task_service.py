from ..models import Task
from ..database import SessionLocal

def get_all_tasks():
    db = SessionLocal()
    return db.query(Task).all()

def create_task(title):
    db = SessionLocal()
    task = Task(title=title)
    db.add(task)
    db.commit()
    return task

def toggle_task(task_id):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.done = not task.done
        db.commit()
    return task
