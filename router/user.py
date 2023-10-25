from fastapi import APIRouter,status,HTTPException

router=APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/user")
def all_user():
    


    return 


