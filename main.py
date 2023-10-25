from fastapi import FastAPI,Response,status
from database import model
from database.db import engine 
from config import settings

# model.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def home():
    print(settings.DB_URL)
    return Response(content=f"Yeh !!! OAuth2 Working")
