from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings, Field


class Settings(BaseSettings):
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: Optional[str] = Field(..., env="NGINX_HOST")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")

    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    POSTGRES_PORT: str = Field(..., env="POSTGRES_PORT")

    REDIS_HOST: str = Field(..., env="REDIS_HOST")
    REDIS_PORT: str = Field(..., env="REDIS_PORT")
    # REDIS_URL: str = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

    CLIENT_ID: str = Field(..., env="CLIENT_ID")
    CLIENT_SECRET: str = Field(..., env="CLIENT_SECRET")

    VERSION: str = Field(..., env="VERSION")


settings = Settings()
