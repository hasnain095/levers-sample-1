import os
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, EmailStr, HttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = "billing"

    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "postgres-db")
    POSTGRES_USER: str = os.getenv("POSTGRES_SERVER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_SERVER", "thefoxjumped")
    POSTGRES_DB: str = os.getenv("POSTGRES_SERVER", "app")
    SQLALCHEMY_DATABASE_URI: str = os.getenv("POSTGRESDSN","postgresql://postgres:thefoxjumped@postgres-db/app")

    class Config:
        case_sensitive = True


# settings = Settings()
settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
