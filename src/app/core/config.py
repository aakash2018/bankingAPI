from pydantic_settings import BaseSettings,SettingsConfigDict
from typing import Literal

class Settings(BaseSettings):
    ENVIRONMENT:Literal["local","staging","production"] = "local"
    
    API_V1_STR:str = "/api/v1"
    PROJECT_NAME:str = "FenTech Bank API"
    PROJECT_DESCRIPTION:str = "Banking FastAPI Project"
    SITE_NAME:str="FenTech Bank"
    DATABASE_URL:str = "postgresql+asyncpg://postgres:mypassword@localhost:5432/fastapi_db"
    
    model_config = SettingsConfigDict(env_file="../../.envs/.env",env_ignore_empty=True,extra="ignore")
settings = Settings()
