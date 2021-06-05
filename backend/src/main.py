from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import routes
from src.config import settings
from src.db import close_mongo_connection, connect_to_mongo


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

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(routes.home_router)
app.include_router(routes.api_router, prefix=settings.API_V1_STR)
