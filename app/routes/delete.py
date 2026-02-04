from fastapi import APIRouter, HTTPException
from datetime import datetime
from bson import ObjectId

from data.database import notes_collection

router = APIRouter()

@router.delete("/delete_notes/{note_id}")
def delete_note(note_id: str):
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID format")

    result = notes_collection.delete_one({"_id": ObjectId(note_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return {
        "message": "Note deleted successfully"
    }

