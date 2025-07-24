from sqlalchemy.orm import Session
from schemas import ProjectCreate, Project
from models import Project as ProjectModel

def create_project(db: Session, project: ProjectCreate) -> Project:
    db_project = ProjectModel(name=project.name, description=project.description)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return Project.from_orm(db_project)

def get_project(db: Session, project_id: int) -> Project:
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if db_project:
        return Project.from_orm(db_project)
    return None
