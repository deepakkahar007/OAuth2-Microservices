from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    APP_URL:str="127.0.0.1"
    APP_PORT:int=8000
    DB_URL:str="localhost:5432"
    DB_NAME:str="oauth2"
    DB_USERNAME:str="deepak"
    DB_PASSWORD:str="deepak"
    JWT_SECRET:str="SuperSecretPassword"
    JWT_EXPIRY:str=""
    JWT_ALGORITHM:str="HS256"

settings=Setting()

# DB_URL:str="postgresql://deepak:deepak@localhost/oauth2"