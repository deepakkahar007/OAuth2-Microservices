from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    APP_URL:str="127.0.0.1"
    PORT:int=8000
    DB_URL:str="postgresql://deepak:deepak@localhost/oauth2"
    DB_NAME:str="oauth2"
    DB_USERNAME:str=""
    DB_PASSWORD:str=""

    


settings=Setting()
