from fastapi import APIRouter
from datetime import datetime

from data.schema import NoteCreate
from data.database import notes_collection

router = APIRouter()

@router.post("/notes")
async def create_note(note: NoteCreate):
    new_note = {
        "title": note.title,
        "content": note.content,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

    result = await notes_collection.insert_one(new_note)

    return {
        "message": "Note created successfully",
        "note_id": str(result.inserted_id)
    }
