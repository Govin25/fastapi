from fastapi import APIRouter,HTTPException,Query,Path
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/users", tags = ["Users"])

users= [{"username":"govind meena",
         "email":"abc@gmail.com",
         "id":1,
         "password":"123ffdgdgd"}]
counter = 2

# how to get the request
class UserCreate(BaseModel):
    username:str
    email:str
    password:str

# how to send the response
class UserResponse(BaseModel):
    id:int
    username:str
    email:str

# [UserResponse, UserResponse]
# UserResponse

@router.post("/")
def create_user(user: UserCreate):
    global counter 
    new_user ={"username": user.username, "email": user.email, "password": user.password,"id": counter}
    users.append(new_user) 
    counter+=1
    return f"data created successfully with id: {counter-1}"


@router.get("/" , response_model=List[UserResponse])
def get_user():
    return users


@router.get("/{user_id}" , response_model=UserResponse)
def get_user(user_id:int = Path(..., ge=0)):
    for user in users:
        if user["id"]==user_id:
            return user
    raise HTTPException(status_code = 404 ,detail="user not found" )


