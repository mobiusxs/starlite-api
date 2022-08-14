from os import environ

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url = environ['DATABASE_URL']


settings = Settings()
