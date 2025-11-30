from fastapi import APIRouter
from ..services.task_service import get_all_tasks, create_task, toggle_task

router = APIRouter(prefix="/tasks")

@router.get("/")
def all_tasks():
    return get_all_tasks()

@router.post("/")
def new_task(data: dict):
    return create_task(data.get("title"))

@router.post("/{task_id}/toggle")
def toggle(task_id: int):
    return toggle_task(task_id)
