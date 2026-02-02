# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # This matches the name "DATABASE_URL" in your .env file
    database_url: str 
    # Add other variables you plan to use, e.g.,
    # api_secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore"
    )

settings = Settings()

