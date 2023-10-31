from pydantic import BaseModel,EmailStr
from typing import Optional

class UserSchema(BaseModel):
    name:str
    email:EmailStr
    phone_no:str
    password:str


class Res_User_Schema(UserSchema):
    id:int
    pass

    class Config:
        from_attributes=True

class Login(BaseModel):
    email:EmailStr
    password:str

class Login_Res(BaseModel):
    name:str
    email:str
    jwt_type:str
    jwt_token:str