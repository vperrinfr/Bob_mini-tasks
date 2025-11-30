from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import TaskCreate, TaskUpdate, TaskResponse
from ..services import task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
async def get_all_tasks(db: AsyncSession = Depends(get_db)):
    """
    Retrieve all tasks.
    
    Returns:
        List of all tasks
    """
    return await task_service.get_all_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a specific task by ID.
    
    Args:
        task_id: ID of the task to retrieve
        
    Returns:
        Task object
    """
    return await task_service.get_task_by_id(db, task_id)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new task.
    
    Args:
        task_data: Task creation data with title
        
    Returns:
        Created task object
    """
    return await task_service.create_task(db, task_data)


@router.patch("/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: AsyncSession = Depends(get_db)
):
    """
    Update an existing task.
    
    Args:
        task_id: ID of the task to update
        task_data: Task update data
        
    Returns:
        Updated task object
    """
    return await task_service.update_task(db, task_id, task_data)


@router.post("/{task_id}/toggle", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def toggle_task(task_id: int, db: AsyncSession = Depends(get_db)):
    """
    Toggle the done status of a task.
    
    Args:
        task_id: ID of the task to toggle
        
    Returns:
        Updated task object
    """
    return await task_service.toggle_task(db, task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete a task.
    
    Args:
        task_id: ID of the task to delete
    """
    await task_service.delete_task(db, task_id)

# Made with Bob
