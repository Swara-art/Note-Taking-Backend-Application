import datetime

from argon2 import hash_password
from fastapi import APIRouter, HTTPException
from data.schema import UserCreate
from data.database import users_collection

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate):
    existing_user = await users_collection.find_one({"email": user.email})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    await users_collection.insert_one({
        "email": user.email,
        "hashed_password": hash_password(user.password),
        "created_at": datetime.utcnow()
    })
    
    return {
        "message": "User created successfully"
    }