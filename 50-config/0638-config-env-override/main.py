import os

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    JsonConfigSettingsSource,
    SettingsConfigDict,
)


class Server(BaseModel):
    host: str = ""
    port: int = 0


class Settings(BaseSettings):
    model_config = SettingsConfigDict(json_file="config.json")

    name: str = "default"
    server: Server = Server()
    hosts: list[str] = []
    debug: bool = False
    retries: int = 0

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        # env_settings first => env vars override the JSON file
        return (env_settings, JsonConfigSettingsSource(settings_cls))


# In-process env var with HIGHER priority than the file overrides `name`.
os.environ["NAME"] = "from-env"

settings = Settings()
print(settings.name)
