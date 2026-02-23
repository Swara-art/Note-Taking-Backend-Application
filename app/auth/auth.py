from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from data.database import users_collection, db
from data.schema import UserCreate, UserLogin
from data.auth_utils import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup", status_code=201)
async def signup(user: UserCreate):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user_doc = {
        "email": user.email,
        "hashed_password": hash_password(user.password),
        "created_at": datetime.utcnow(),
    }

    result = await users_collection.insert_one(user_doc)

    return {
        "message": "User created successfully",
        "user_id": str(result.inserted_id),
    }


@router.post("/login")
async def login(user: UserLogin):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(str(db_user["_id"]))
    return {"access_token": token, "token_type": "bearer"}