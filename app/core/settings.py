from pydantic_settings import BaseSettings, SettingsConfigDict
import dotenv

class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='POSTGRES_', extra='ignore')

    PASSWORD: str
    USER: str
    DB: str
    HOST: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

    db: DBSettings



def get_settings():
    dotenv.load_dotenv()
    return Settings()