from fastapi import APIRouter, HTTPException, Depends, HTTPException, status
from datetime import datetime
from data.database import db
from data.schema import UserCreate, UserLogin
from data.auth_utils import hash_password, verify_password, create_access_token
import os
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

users_collection = db[os.getenv("USERS_COLLECTION")]


@router.post("/signup")
async def signup(user: UserCreate):
    if await users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    await users_collection.insert_one({
        "email": user.email,
        "hashed_password": hash_password(user.password),
        "created_at": datetime.utcnow()
    })

    return {"message": "User registered successfully"}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = await users_collection.find_one({"email": form_data.username})

    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not verify_password(form_data.password, db_user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(str(db_user["_id"]))
    return {"access_token": token, "token_type": "bearer"}
