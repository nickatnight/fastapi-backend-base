from fastapi import FastAPI

from src.api import health


app = FastAPI()

app.include_router(health.router)
