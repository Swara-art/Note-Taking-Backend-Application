from argon2 import verify_password
from fastapi import APIRouter, HTTPException, Depends
from data.schema import UserLogin 
from data.database import users_collection
from auth.auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = await users_collection.find_one(
        {"email": form_data.username}
    )

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(form_data.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(str(db_user["_id"]))

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    

    