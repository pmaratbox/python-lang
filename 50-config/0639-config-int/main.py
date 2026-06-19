from pydantic_settings import BaseSettings, SettingsConfigDict, JsonConfigSettingsSource
from pydantic import BaseModel


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
    missing: str = "fallback"

    @classmethod
    def settings_customise_sources(
        cls, settings_cls, init_settings, env_settings, dotenv_settings, file_secret_settings
    ):
        # env_settings first so env vars override the JSON file
        return (env_settings, JsonConfigSettingsSource(settings_cls))


s = Settings()
print(s.retries)
