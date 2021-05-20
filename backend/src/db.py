from databases import Database
from sqlalchemy import create_engine, MetaData

from src.config import settings


# SQLAlchemy
engine = create_engine(settings.POSTGRES_URL, pool_size=3, max_overflow=0)
metadata = MetaData()

# databases query builder
database = Database(settings.POSTGRES_URL)
