from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
NOTES_COLLECTION = os.getenv("NOTES_COLLECTION")
USERS_COLLECTION = os.getenv("USERS_COLLECTION")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing in .env")
if not DB_NAME:
    raise ValueError("DB_NAME is missing in .env")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

notes_collection = db[NOTES_COLLECTION]
users_collection = db[USERS_COLLECTION]