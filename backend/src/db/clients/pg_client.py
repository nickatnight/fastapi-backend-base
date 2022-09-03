from typing import List, TypeVar

from r_dogecoin_bot.clients.database import AbstractDbClient
from r_dogecoin_bot.main import asyncpraw
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.db.session import async_session, get_session
from src.models import Meme


Submission = TypeVar("Submission")


class PostgresSubmissionDbClient(AbstractDbClient[asyncpraw.models.Submission, AsyncSession, Meme]):
    session: AsyncSession = get_session()
    schema: Meme = Meme

    @classmethod
    async def process(cls, model: asyncpraw.models.Submission) -> None:
        async with async_session() as session:
            my_model: Meme = cls.schema(
                **{
                    "submission_title": model.title,
                    "submission_url": model.url,
                    "submission_id": model.id,
                    "permalink": model.permalink,
                    "author": model.author.name,
                    "timestamp": model.created_utc,
                }
            )
            session.add(my_model)
            await session.commit()
            await session.refresh(my_model)

    @classmethod
    async def get_existing_ids(cls) -> List[str]:
        async with async_session() as session:
            result = await session.execute(select(Meme.submission_id))

        return result.scalars().all()
