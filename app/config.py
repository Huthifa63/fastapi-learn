from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # 👇 هذا الأساسي على Render
    database_url: Optional[str] = None

    # 👇 خليه Optional عشان ما يطلبهم إذا DATABASE_URL موجود
    database_username: Optional[str] = None
    database_password: Optional[str] = None
    database_hostname: Optional[str] = None
    database_port: Optional[str] = None
    database_name: Optional[str] = None

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings() # type: ignore
