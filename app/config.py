from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class Settings(BaseSettings):
    # يقرأ من .env ويسمح بمتغيرات زيادة بدون ما يخرب
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # موجودين في .env عندك
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str

    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # نحسب database_url تلقائياً من القيم اللي فوق
    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.database_username}:{self.database_password}"
            f"@{self.database_hostname}:{self.database_port}/{self.database_name}"
        )


settings = Settings() # type: ignore
