from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool
    DATABASE_UTL: str


    class Config:
        env_file = ".env"

Settings = Settings()