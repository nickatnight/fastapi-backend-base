from fastapi import FastAPI

from src.api import routes
from src.config import settings
from src.db import engine, database, metadata


metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(routes.api_router, prefix=settings.API_V1_STR)
