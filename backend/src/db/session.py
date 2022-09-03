import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.db.utils import get_db_url


logger = logging.getLogger(__name__)
DB_POOL_SIZE = 83
WEB_CONCURRENCY = 9
POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)
POSTGRES_URL = get_db_url()

engine = create_async_engine(
    POSTGRES_URL, echo=True, future=True, pool_size=POOL_SIZE, max_overflow=64
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def on_startup():
    logger.info("FastAPI app running...")


# async def add_postgresql_extension() -> None:
#     async with db():
#         query = text("CREATE EXTENSION IF NOT EXISTS pg_trgm")
#         return await db.session.execute(query)


async def get_session() -> AsyncSession:
    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async with async_session() as session:
        yield session
