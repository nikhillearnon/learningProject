from sqlalchemy import Column, String, Integer, Boolean, DateTime,Text
from datetime import datetime
from app.db.base import Base

class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    deadline = Column(DateTime, default=datetime.now)
    created_at = Column(DateTime, default=datetime.now)
