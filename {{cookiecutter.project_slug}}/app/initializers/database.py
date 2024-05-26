from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from app.settings import get_settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

async_engine = create_async_engine(get_settings().database_url, echo=False)

AsyncSessionFactory = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Open a new async session with the database.

    Closes the session after use.
    """
    async with AsyncSessionFactory() as session:
        yield session
