from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MySettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    OPENAI_API_KEY: str = Field(env='OPENAI_API_KEY')
    SERPER_API_KEY: str = Field(env='SERPER_API_KEY')
    OPENAI_MODEL_NAME: str = Field(env='OPENAI_MODEL_NAME')
    SUNO_API_CUSTOM_GENERATE_URL: str = Field(env='SUNO_API_CUSTOM_GENERATE_URL')
    MAIL_USERNAME: str = Field(env='MAIL_USERNAME')
    MAIL_PASSWORD: str = Field(env='MAIL_PASSWORD')
    DB_URL: str = Field(env='DB_URL')
    HUNTER_IO_API_KEY: str = Field(env='HUNTER_IO_API_KEY')
    TOPMEDIA_API_KEY: str = Field(env='TOPMEDIA_API_KEY')
    CLOUDINARY_URL: str = Field(env='CLOUDINARY_URL')
    CLOUDINARY_NAME: str = Field(env='CLOUDINARY_NAME')
    CLOUDINARY_API_KEY: str = Field(env='CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET: str = Field(env='CLOUDINARY_API_SECRET')
    VIMEO_TOKEN: str = Field(env='VIMEO_TOKEN')
    VIMEO_KEY: str = Field(env='VIMEO_KEY')
    VIMEO_SECRET: str = Field(env='VIMEO_SECRET')
    SUNO_COOKIE: str = Field(env='SUNO_COOKIE')
    BROWSERLESS_URL: str = Field(env='BROWSERLESS_URL')


settings = MySettings()


