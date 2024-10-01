from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    TG_token_bot: str

    @property
    def TG_token_bot(self) -> str:
        return self.TG_token_bot

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
