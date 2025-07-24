from sqlalchemy.orm import Session
from schemas import TaskCreate, Task
from models import Task as TaskModel

def create_task(db: Session, task: TaskCreate) -> Task:
    db_task = TaskModel(title=task.title, description=task.description, project_id=task.project_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return Task.from_orm(db_task)

def get_task(db: Session, task_id: int) -> Task:
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task:
        return Task.from_orm(db_task)
    return None
