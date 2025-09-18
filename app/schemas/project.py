from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class ProjectCreate(BaseModel):
    title: str
    description: str
    deadline: date

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[date] = None

