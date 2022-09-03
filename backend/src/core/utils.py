from r_dogecoin_bot.main import DogecoinMemeBot
from r_dogecoin_bot.types import RedditClientConfig

from src.db.clients.pg_client import PostgresSubmissionDbClient


async def botnet_run():
    reddit_config: RedditClientConfig = dict(
        client_id="PPeWD0Gn3eKR4A",
        client_secret="W_DxGMrD21uk-MNt1R60-9NP_qpEzQ",
        user_agent="to_the_moon",
    )
    bot = DogecoinMemeBot(
        reddit_client_config=reddit_config,
        db_client=PostgresSubmissionDbClient,
    )

    await bot.run()
