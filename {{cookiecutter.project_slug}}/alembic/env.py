import asyncio
from logging.config import fileConfig

from alembic import context
from app.models.base import Base
from app.models.user import *
from app.settings.settings import get_settings
from sqlalchemy.ext.asyncio import create_async_engine

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
target_metadata = Base.metadata
config.set_main_option(
    'sqlalchemy.url', get_settings().database_url.get_secret_value(),
)


async def run_migrations_online() -> None:
    connectable = create_async_engine(
        config.get_main_option('sqlalchemy.url'),
        future=True,
        echo=True,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_as_batch=True,
        asynchronous=True,
    )

    with context.begin_transaction():
        context.run_migrations()


asyncio.run(run_migrations_online())
