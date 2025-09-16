# app/core/config.py  -- for pydantic v2 + pydantic-settings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # tell Settings to read .env
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
