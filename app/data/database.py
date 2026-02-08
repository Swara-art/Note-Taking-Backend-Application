# I want to use aynchronous programming with MongoDB, so I will use the Motor library, which is an asynchronous driver for MongoDB.
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

import os

client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]
notes_collection = db[(os.getenv("COLLECTION"))]



