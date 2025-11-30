from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """Base schema for Task with common attributes"""
    title: str = Field(..., min_length=1, max_length=200, description="Task title")


class TaskCreate(TaskBase):
    """Schema for creating a new task"""
    pass


class TaskUpdate(BaseModel):
    """Schema for updating a task"""
    title: str | None = Field(None, min_length=1, max_length=200)
    done: bool | None = None


class TaskResponse(TaskBase):
    """Schema for task responses"""
    id: int
    done: bool

    class Config:
        from_attributes = True

# Made with Bob
