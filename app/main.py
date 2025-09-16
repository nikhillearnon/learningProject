from fastapi import FastAPI
from app.api.v1 import auth, users
from app.core.config import settings

app = FastAPI(title="FastAPI Auth Example")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
def home():
    return {"app": "fastapi-project", "environment": settings.DATABASE_URL}
