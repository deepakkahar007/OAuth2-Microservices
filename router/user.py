from fastapi import APIRouter,status,HTTPException,Depends,Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
from database import db,model,schema
from typing import List

router=APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/all",response_model=List[schema.Res_User_Schema])
def all_user(db:Session=Depends(db.get_db)):
    user=db.query(model.UserModel).all()
    return user

@router.post("/register",status_code=status.HTTP_201_CREATED,response_model=schema.Res_User_Schema)
def create_user(body:schema.UserSchema,db:Session=Depends(db.get_db)):
   
    if body.name=="" or body.email=="" or body.phone_no=="" or body.password=="":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                           detail={"msg":"all details not found","inputed_data":body.model_dump()})
    else:
        _user_exist=db.query(exists().where(model.UserModel.email==body.email)).scalar()

        if _user_exist:
          raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                              detail={"msg":"email already exists","inputed_data":body.model_dump()})
        else:
            new_user=model.UserModel(**body.model_dump())
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return Response(status_code=status.HTTP_201_CREATED, 
                            content=f"User Created Successfully")

@router.get("/user_id/{id:int}",response_model=schema.Res_User_Schema)
def get_by_id(id,db:Session=Depends(db.get_db)):
    _id=db.query(model.UserModel).filter(model.UserModel.id==id)
   
    if _id.first()==None:
        return Response(status_code=404,content=f"no id found with this {id} id")

    return _id.first()

@router.delete("/delete_id/{id:int}")
def delete_user(id,db:Session=Depends(db.get_db)):
    _id=db.query(model.UserModel).filter(model.UserModel.id==id)
    
    if _id.first() == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND,
                        content=f"No id found with this {id} id")
    
    
    _id.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

