from pydantic import Field, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    storage_path: DirectoryPath = Field(..., env="STORAGE_PATH")
    chat_id: int = Field(..., env="CHAT_ID")
    bot_token: str = Field(..., env="BOT_TOKEN")

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

settings = Settings()
