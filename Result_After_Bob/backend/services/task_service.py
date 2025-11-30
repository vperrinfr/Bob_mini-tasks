from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from ..models import Task
from ..schemas import TaskCreate, TaskUpdate


async def get_all_tasks(db: AsyncSession) -> list[Task]:
    """
    Retrieve all tasks from the database.
    
    Args:
        db: Database session
        
    Returns:
        List of all tasks
    """
    result = await db.execute(select(Task).order_by(Task.id))
    return list(result.scalars().all())


async def get_task_by_id(db: AsyncSession, task_id: int) -> Task:
    """
    Retrieve a single task by ID.
    
    Args:
        db: Database session
        task_id: ID of the task to retrieve
        
    Returns:
        Task object
        
    Raises:
        HTTPException: If task not found
    """
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    
    return task


async def create_task(db: AsyncSession, task_data: TaskCreate) -> Task:
    """
    Create a new task.
    
    Args:
        db: Database session
        task_data: Task creation data
        
    Returns:
        Created task object
    """
    task = Task(title=task_data.title.strip(), done=False)
    db.add(task)
    await db.flush()
    await db.refresh(task)
    return task


async def update_task(db: AsyncSession, task_id: int, task_data: TaskUpdate) -> Task:
    """
    Update an existing task.
    
    Args:
        db: Database session
        task_id: ID of the task to update
        task_data: Task update data
        
    Returns:
        Updated task object
        
    Raises:
        HTTPException: If task not found
    """
    task = await get_task_by_id(db, task_id)
    
    if task_data.title is not None:
        task.title = task_data.title.strip()
    if task_data.done is not None:
        task.done = task_data.done
    
    await db.flush()
    await db.refresh(task)
    return task


async def toggle_task(db: AsyncSession, task_id: int) -> Task:
    """
    Toggle the done status of a task.
    
    Args:
        db: Database session
        task_id: ID of the task to toggle
        
    Returns:
        Updated task object
        
    Raises:
        HTTPException: If task not found
    """
    task = await get_task_by_id(db, task_id)
    task.done = not task.done
    await db.flush()
    await db.refresh(task)
    return task


async def delete_task(db: AsyncSession, task_id: int) -> None:
    """
    Delete a task.
    
    Args:
        db: Database session
        task_id: ID of the task to delete
        
    Raises:
        HTTPException: If task not found
    """
    task = await get_task_by_id(db, task_id)
    await db.delete(task)
    await db.flush()

# Made with Bob
