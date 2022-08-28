from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import routes
from src.db.session import init_db
from src.core.config import settings


tags_metadata = [
    {
        "name": "health",
        "description": "Health check for api",
    },
]

app = FastAPI(
    title="fastapi-backend-base",
    description="base project for fastapi backend",
    version=settings.VERSION,
    openapi_tags=tags_metadata,
)


app.add_middleware(CORSMiddleware, allow_origins=["*"])

app.add_event_handler("startup", init_db)

app.include_router(routes.home_router)
app.include_router(routes.api_router, prefix=settings.API_V1_STR)
