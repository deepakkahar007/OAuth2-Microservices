from fastapi import APIRouter,Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
from database import db,model,schema


router=APIRouter(prefix="/auth",tags=['auth'])

@router.post("/login",)
def login(user:schema.Login,db:Session=Depends(db.get_db)):
    print(user.email,user.password)


    return f"login user"



