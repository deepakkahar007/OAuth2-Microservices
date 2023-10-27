from fastapi import APIRouter,status,HTTPException,Depends,Response
from sqlalchemy.orm import Session
from database import db,model,schema


router=APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/all")
def all_user(db:Session=Depends(db.get_db)):
    user=db.query(model.UserModel).all()
    return user

@router.post("/create",status_code=status.HTTP_201_CREATED,response_model=schema.Res_User_Schema)
def create_user(body:schema.UserSchema,db:Session=Depends(db.get_db)):
    try:
        new_user=model.UserModel(**body.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                           detail={"msg":"some error occured","inputed_data":body.model_dump()})

@router.get("/user_id/{id:int}",response_model=schema.Res_User_Schema)
def get_by_id(id,db:Session=Depends(db.get_db)):
    _id=db.query(model.UserModel).filter(model.UserModel.id==id)

    if _id.first()==None:
        return Response(status_code=404,content=f"no id found with this {id} id")

    return _id.first()

