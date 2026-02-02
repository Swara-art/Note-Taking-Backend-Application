from pymongo import MongoClient
import os

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION = os.getenv("COLLECTION")

client = MongoClient(MONGODB_URI)
database = client[DB_NAME]
notes_collection = database[COLLECTION]
