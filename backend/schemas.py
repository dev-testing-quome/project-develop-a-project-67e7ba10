from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str]

class Project(BaseModel):
    id: int
    name: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    owner_id: int

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]
    project_id: int

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    project_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
