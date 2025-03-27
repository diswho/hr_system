from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "HR System API"
    app_version: str = "0.1.0"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/hr_system"
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()