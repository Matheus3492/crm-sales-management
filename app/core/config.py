from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CRM Sales Management"
    app_version: str = "0.1.0"
    debug: bool = False


settings = Settings()