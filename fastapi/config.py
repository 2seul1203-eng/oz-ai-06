# configuration: 구성; 설정

from pydantic_settings import BaseSettings, SettingsConfigDict

# 설정 값을 관리하는 클래스
class Settings(BaseSettings):
    openai_api_key: str

    # .env 파일을 읽어서 settiongs 값을 채워줌
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
