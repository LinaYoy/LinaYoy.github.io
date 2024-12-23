import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/data/db.sqlite3"
    SECRET_KEY: str
    ALGORITHM: str
    BOT_TOKEN: str  # добавлено
    CHAT_ID: int    # добавлено

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")

settings = Settings()  # Получение настроек
database_url = settings.DB_URL