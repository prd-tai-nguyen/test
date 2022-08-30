import secrets

from typing import Any

from pydantic import AnyHttpUrl, \
    BaseSettings, \
    HttpUrl, \
    validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "scrape"

    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    SERVER_NAME: str

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls,
                              v: str | list[str],
                              ) -> str | list[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    MYSQL_HOST: str
    MYSQL_DATABASE: str = "scrape-master"
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_PORT: str

    DB_URI: str | None

    @validator("DB_URI", pre=True)
    def assemble_db_uri(cls,
                        v: str,
                        values: dict[str, Any]) -> str | None:
        if isinstance(v, str):
            return v
        return (f'mysql+mysqldb://{values.get("MYSQL_USER")}'
                f':{values.get("MYSQL_PASSWORD")}'
                f'@{values.get("MYSQL_HOST")}:{values.get("MYSQL_PORT")}'
                f'/{values.get("MYSQL_DATABASE")}')

    SENTRY_DSN: HttpUrl | None = None

    # @validator("SENTRY_DSN", pre=True)
    # def sentry_dsn_can_be_blank(cls, v: str) -> str | None:
    #     if len(v) == 0:
    #         return None
    #     return v

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
