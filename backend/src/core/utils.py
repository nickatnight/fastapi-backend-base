from r_dogecoin_bot.main import DogecoinMemeBot
from r_dogecoin_bot.types import RedditClientConfig

from src.core.config import settings
from src.db.clients.pg_client import PostgresSubmissionDbClient


async def botnet_run():
    reddit_config: RedditClientConfig = dict(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        user_agent="to_the_moon",
    )
    bot = DogecoinMemeBot(
        reddit_client_config=reddit_config,
        db_client=PostgresSubmissionDbClient,
    )

    await bot.run()
