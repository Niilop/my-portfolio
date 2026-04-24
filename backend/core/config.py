from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Niilo Paakkonen | Portfolio"
    app_env: str = "production"
    debug: bool = False
    contact_email: str = ""
    cors_origins: list[str] = ["*"]

    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
