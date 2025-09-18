from fastapi import APIRouter, Depends, HTTPException, status
from app.api.deps import get_db
from sqlalchemy.orm import Session
# from schemas.project import ProjectCreate
from app.schemas.project import ProjectCreate
from app.crud.project_crud import create_project as create_project_crud
from app.crud.project_crud import update_project as update_project_crud
from app.crud.project_crud import delete_project as delete_project_crud

router = APIRouter()

@router.post('/create')
def create_project(project_in: ProjectCreate, db: Session = Depends(get_db)):
    return create_project_crud(db, project_in)

@router.put("/update/{project_id}")
def update_project(
        project_id: int,
        project_in: ProjectCreate, 
        db: Session = Depends(get_db)
    ):
    updated = update_project_crud(project_id,db, project_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated

@router.delete("/projects/{project_id}", status_code=204)
def delete_project_endpoint(project_id: int, db: Session = Depends(get_db)):
    success = delete_project_crud(db, project_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return None  