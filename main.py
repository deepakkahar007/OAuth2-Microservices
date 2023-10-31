from fastapi import FastAPI,Response
from router import user,auth

app=FastAPI()

app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return Response(content=f"Yeh !!! OAuth2 Working")

# activate env source /home/deepak/Documents/fastAPI/env/bin/activate

