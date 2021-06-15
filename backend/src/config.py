import secrets
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings, Field


class Settings(BaseSettings):
    API_V1_STR: str = "/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: Optional[str] = Field(..., env="NGINX_HOST")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")

    MONGODB_HOST: str = Field(..., env="MONGODB_HOST")
    MONGODB_USER: str = Field(..., env="MONGODB_USER")
    MONGODB_PASS: str = Field(..., env="MONGODB_PASS")
    MONGODB_DATABASE: str = Field(..., env="MONGODB_DATABASE")

    REDIS_HOST: str = Field(..., env="REDIS_HOST")

    VERSION: str = Field(..., env="VERSION")


settings = Settings()
