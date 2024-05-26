from functools import lru_cache

from app.settings.logging_config import construct_logging_config
from pydantic import Field
from pydantic import HttpUrl
from pydantic import model_validator
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from typing_extensions import Self


class Settings(BaseSettings):
    """Contains various application settings."""
    app_name: str = Field(default='app')
    app_host: str = Field(default='0.0.0.0')  # noqa: S104
    app_port: int = Field(default=8000)  # noqa: 8000

    secret_key: SecretStr = Field(default=...)

    environment: str = Field(default='development')
    testing: bool = Field(default=False)
    sentry_dsn: HttpUrl | None = Field(default=None)
    sentry_enabled: bool = Field(default=False)

    database_url: SecretStr = Field(default=...)

    log_level: str = Field(default='DEBUG')  # noqa: WPS432
    log_format: str = Field(default='colored', alias='log_format')
    log_config: dict = Field(default_factory=dict, alias='log_config')

    model_config = SettingsConfigDict(
        env_file='.env',
    )

    @model_validator(mode='after')
    def override_deafult_config(self) -> Self:  # noqa: N805
        """Sets the default logging configuration."""
        if self.log_config:
            return self
        self.log_config = construct_logging_config(
            self.log_level,
            self.app_name,
            self.log_format,
        )
        return self


@lru_cache
def get_settings() -> Settings:
    """Loads environment variables."""
    return Settings()
