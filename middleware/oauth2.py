# from fastapi import Depends,status,HTTPException
# from fastapi.security.oauth2 import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from datetime import datetime, timedelta
# from sqlalchemy.orm import Session
# from . import schema, db, model

# oauth2_scheme=OAuth2PasswordBearer(tokenUrl='jwt')

# SECRET_KEY="hello"
# ALGORITHM="HS256"
# ACCESS_TOKEN_EXPIRY_MINUTE=120

# def create_access_token(data:dict):
#     to_encode = data.copy()
#     expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTE)
#     to_encode.update({"exp":expire})
#     encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
#     return encoded_jwt

# def verify_token(token:str,cred_exception):
#     try:
#         payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
#         id = payload.get("user_id")
#         if id is None:
#             raise cred_exception
#         token_data=schema.Token_res(id=id)
#     except JWTError:
#         raise cred_exception
#     return token_data
    
# def get_current_user(token:str=Depends(oauth2_scheme), db:Session=Depends(db.get_db)):
#     cred_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                  detail=f"could not validate credentials",
#                                  headers={'WWW.Authenticate':"Bearer"})

#     token=verify_token(token,cred_exception) # type: ignore

#     user= db.query(model.User).filter(model.User.id==token.id).first()
#     return user


