from functools import lru_cache
from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    DB_SCHEME: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_NAME: str
    DB_POOL_SIZE: int

    SERVER_HOST: str = "127.0.0.1"
    SERVER_PORT: int = 5005

    POSTGRES_INDEXES_NAMING_CONVENTION = {
        "ix": "%(column_0_label)s_idx",
        "uq": "%(table_name)s_%(column_0_name)s_key",
        "ck": "%(table_name)s_%(constraint_name)s_check",
        "fk": "%(table_name)s_%(column_0_name)s_fkey",
        "pk": "%(table_name)s_pkey",
    }

    @property
    def database_url(self):
        return f"{self.DB_SCHEME}://{self.DB_USER}:{self.DB_PASSWORD.get_secret_value()}" \
               f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


@lru_cache()
def get_config() -> Settings:
    return Settings()
