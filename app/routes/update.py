from fastapi import APIRouter, HTTPException
from datetime import datetime
from bson import ObjectId

from data.database import notes_collection

router = APIRouter()

@router.put("/update_notes/{note_id}")
def update_note(note_id: str, title: str = None, content: str = None):

    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID format")

    updated_fields = {}

    if title is not None:
        updated_fields["title"] = title

    if content is not None:
        updated_fields["content"] = content

    updated_fields["updated_at"] = datetime.utcnow()

    result = notes_collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": updated_fields}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return {
        "message": "Note updated successfully"
    }
