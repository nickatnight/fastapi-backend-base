from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from src.core.config import settings


DB_POOL_SIZE = 83
WEB_CONCURRENCY = 9
POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)
POSTGRES_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"  # noqa

engine = create_async_engine(
    POSTGRES_URL, echo=True, future=True, pool_size=POOL_SIZE, max_overflow=64
)


async def on_startup():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


# async def add_postgresql_extension() -> None:
#     async with db():
#         query = text("CREATE EXTENSION IF NOT EXISTS pg_trgm")
#         return await db.session.execute(query)


async def get_session() -> AsyncSession:
    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError as sql_ex:
            await session.rollback()
            raise sql_ex
        except HTTPException as http_ex:
            await session.rollback()
            raise http_ex
        finally:
            await session.close()
