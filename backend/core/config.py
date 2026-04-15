from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os

class Settings(BaseSettings):
    # App Settings
    app_name: str = "Smart File Organizer Pro"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = False

    # Database Settings
    database_url: str = "sqlite:///./file_organizer.db"

    # AI Settings
    ollama_base_url: str = "http://localhost:11434"
    llm_model: str = "llama3.2"

    # File Watcher Settings
    default_watch_path: str = os.path.expanduser("~/Downloads")

    # Storage Settings
    storage_path: str = os.path.expanduser("~/SmartFileOrganizer")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
