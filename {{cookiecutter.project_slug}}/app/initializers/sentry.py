import tomllib
from functools import lru_cache

from sentry_sdk import init as sentry_init
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

from app.initializers.logger import get_logger
from app.settings import get_settings

settings = get_settings()
logger = get_logger('uvicorn')


def init(include_integrations=True) -> None:
    """Wrapper function to initialize Sentry with arguments."""
    is_disabled = (
        not settings.sentry_enabled
        or settings.testing
        or settings.sentry_dsn is None
    )
    if is_disabled:
        logger.info('Sentry disabled.')
        return
    logger.info('Enabling Sentry...')
    integrations = []
    if include_integrations:
        integrations = [FastApiIntegration(), StarletteIntegration()]
    sentry_init(
        environment=settings.environment,
        dsn=settings.sentry_dsn,  # type: ignore
        traces_sample_rate=1.0,
        integrations=integrations,
        release=get_app_version(),
    )


@lru_cache
def get_app_version() -> str:
    """Read app version from the pyproject.toml file."""
    with open('pyproject.toml', 'rb') as pfile:
        pyproject = tomllib.load(pfile)
        version = pyproject['tool']['poetry']['version']
    return f'{{cookiecutter.project_slug}}@{version}'

