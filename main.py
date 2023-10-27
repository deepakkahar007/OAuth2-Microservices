from fastapi import FastAPI,Response,status
from database import model
from database.db import engine 
from config import settings
from router import user,auth

model.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(user.router)
# app.include_router(auth.router)


@app.get("/")
def home():
    print(settings.DB_URL)
    return Response(content=f"Yeh !!! OAuth2 Working")

# activate env source /home/deepak/Documents/fastAPI/env/bin/activate

