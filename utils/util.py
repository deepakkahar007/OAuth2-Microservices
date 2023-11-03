from fastapi import Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from config import settings
from database import db,model

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')

pwd_context=CryptContext(schemes=['bcrypt'],deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(password,hashed_password):
    return pwd_context.verify(password,hashed_password)

def create_jwt(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRY)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,settings.JWT_SECRET,algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def verify_jwt(token:str,cred_expception):
    try:
        payload=jwt.decode(token,settings.JWT_SECRET,algorithms=settings.JWT_ALGORITHM)
        id=payload.get("_id")
        if id is None:
            raise cred_expception

    except JWTError:
        raise cred_expception   

    return id

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(db.get_db)):
    cred_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                 detail=f"could not validate credentials",
                                 headers={"WWW.Authenticate":"Bearer"})
    
    token=verify_jwt(token,cred_exception)
    user=db.query(model.UserModel).filter(model.UserModel.id==token.id).first()
    
    return user

