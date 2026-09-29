from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    hindsight_base_url: str = "https://api.hindsight.vectorize.io"
    hindsight_api_key: str | None = None
    hindsight_bank_id: str = "project-zero-demo"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
