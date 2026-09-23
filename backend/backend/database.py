from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from backend.config import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_async_engine(str(DATABASE_URL), echo=True)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
Base = declarative_base()
