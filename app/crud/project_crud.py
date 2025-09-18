from sqlalchemy.orm import Session
from app.models.project import Projects 
# from app.core.security import get_password_hash, verify_password
# from typing import Optional
from datetime import date
from app.schemas.project import ProjectCreate

# def get_user_by_email(db: Session, email: str) -> Optional[User]:
#     return db.query(User).filter(User.email == email).first()

# def get_user(db: Session, user_id: int) -> Optional[User]:
#     return db.query(User).get(user_id)

# def create_project(db: Session, *, title: str, description: str, deadline: date) -> Projects:
#     db_project = Projects(
#             title=title, 
#             description=description,
#             deadline=deadline
#         )
#     db.add(db_project)
#     db.commit()
#     db.refresh(db_project)
#     return db_project


def create_project(db: Session, project_in: ProjectCreate) -> Projects:
    db_project = Projects(**project_in.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(project_id: int,db: Session, project_in: ProjectCreate) -> Projects:
    db_project = db.query(Projects).filter(Projects.id == project_id).first()

    if not db_project:
        return None
    
    if project_in.title is not None:
        db_project.title = project_in.title

    if project_in.description is not None:
        db_project.description = project_in.description

    if project_in.deadline is not None:
        db_project.deadline = project_in.deadline

    # db_project.title = 
    # db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int) -> bool:
    db_project = db.query(Projects).filter(Projects.id == project_id).first()
    
    if not db_project:
        return False

    db.delete(db_project)
    db.commit()
    return True





# def update_todo(todo_id: int, todo: TodoSchema, db: Session = Depends(get_db)):
#     db_todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
#     if not db_todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     db_todo.title = todo.title
#     db_todo.completed = todo.completed
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo

# def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
#     user = get_user_by_email(db, email)
#     if not user:
#         return None
#     if not verify_password(password, user.hashed_password):
#         return None
#     return user
