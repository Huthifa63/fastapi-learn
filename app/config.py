from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_port: str
    database_name: str

    database_url: Optional[str] = None   # ✅ أضفنا هذا

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings() # type: ignore
