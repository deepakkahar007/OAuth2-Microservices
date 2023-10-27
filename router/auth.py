# from fastapi import APIRouter,Depends,status,HTTPException,Response
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from .. import schema,model,db,oauth2
# from ..utils import verify

# router=APIRouter(
#     prefix='/auth',
#     tags=['authentication']
# )

# @router.post("/jwt", response_model=schema.Token)
# def auth_route(user:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(db.get_db)):

#     u=db.query(model.User).filter(model.User.email==user.username).first()

#     if u == None :
#         return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"no user found with this {user.username} email")
    
#     if not verify(user.password,u.password):
#         return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                              detail=f"password not matched, try again")

#     access_token=oauth2.create_access_token(data={"user_id":u.id,"email":u.email})

#     return {"jwt_token":access_token,"token_type":"Bearer"}