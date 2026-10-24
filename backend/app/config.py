from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Hararghe AgroAlert AI"
    environment: str = "development"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/hararghe_ai"
    secret_key: str = "change-me-in-production"
    cors_origins: str = "http://localhost:5173,http://localhost:19006"

    class Config:
        env_file = ".env"


settings = Settings()
