from data.database import notes_collection
from datetime import datetime

note = {
    "title": "My Backend Note",
    "content": "This note was inserted from FastAPI",
    "created_at": datetime.utcnow(),
    "updated_at": datetime.utcnow()
}

result = notes_collection.insert_one(note)
print(result.inserted_id)
