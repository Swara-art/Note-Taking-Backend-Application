from fastapi import APIRouter, HTTPException
from bson import ObjectId
from bson.errors import InvalidId

from data.database import notes_collection

router = APIRouter()

@router.get("/read_notes")
async def read_notes():
    notes = []
    async for note in notes_collection.find():
        note["_id"] = str(note["_id"])
        notes.append({
            "id": note["_id"],
            "title": note["title"],
            "content": note["content"],
            "created_at": note["created_at"],
            "updated_at": note["updated_at"]
        })
    return notes

@router.get("/read_notes/{note_id}")
async def read_note_id(note_id: str):
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID format")
    note = await notes_collection.find_one({"_id": ObjectId(note_id)})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    note["_id"] = str(note["_id"])
    return {
        "id": note["_id"],
        "title": note["title"],
        "content": note["content"],
        "created_at": note["created_at"],
        "updated_at": note["updated_at"]
    }

