from fastapi import APIRouter,Depends,HTTPException,status,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import db,model,schema
from utils import util


router=APIRouter(prefix="/auth",tags=['auth'])

@router.post("/login",)
def login(response:Response,
          user:OAuth2PasswordRequestForm=Depends(),
          db:Session=Depends(db.get_db)):
    
    _user=db.query(model.UserModel).filter(model.UserModel.email==user.username).first()

    if _user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"no user found with this {user.username} email")
    else:
        if util.verify_password(user.password,_user.password):
            jwt_token=util.create_jwt(data={"_id":_user.id,"email":_user.email})
            response.set_cookie(key="Bearer",value=jwt_token)
            return {"msg":"Login Success","token":jwt_token,"token_type":"Bearer"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f"password not matched try again !")

