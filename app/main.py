from fastapi import FastAPI
from app.api.v1 import auth, users,projects
from app.core.config import settings

app = FastAPI(title="FastAPI Auth Example")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication - auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Authentication - users"])
app.include_router(projects.router, prefix="/api/v1/project", tags=["Project"])

@app.get("/")
def home():
    return {"app": "fastapi-project", "environment": settings.DATABASE_URL}
