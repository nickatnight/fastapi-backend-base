import aioredis
from fastapi_limiter import FastAPILimiter

from motor.motor_asyncio import AsyncIOMotorClient
from src.config import settings


MONGODB_URL = f"mongodb://{settings.MONGODB_USER}:{settings.MONGODB_PASS}@{settings.MONGODB_HOST}:27017/{settings.MONGODB_DATABASE}"  # noqa


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client[settings.MONGODB_DATABASE]


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(MONGODB_URL, maxPoolSize=3, minPoolSize=0)
    redis = await aioredis.create_redis_pool(settings.REDIS_HOST)

    await FastAPILimiter.init(redis)


async def close_mongo_connection():
    db.client.close()
