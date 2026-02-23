from datetime import datetime

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from data.database import notes_collection
from data.schema import NoteCreate, NoteUpdate
from data.auth_utils import get_current_user_id

router = APIRouter(prefix="/notes", tags=["Notes"])


def _to_note_response(note: dict) -> dict:
    return {
        "id": str(note["_id"]),
        "user_id": str(note["user_id"]),
        "title": note["title"],
        "content": note["content"],
        "created_at": note["created_at"],
        "updated_at": note["updated_at"],
    }


@router.post("/", status_code=201)
async def create_note(note: NoteCreate, user_id=Depends(get_current_user_id)):
    now = datetime.utcnow()
    doc = {
        "user_id": user_id,
        "title": note.title,
        "content": note.content,
        "created_at": now,
        "updated_at": now,
    }
    result = await notes_collection.insert_one(doc)
    return {"note_id": str(result.inserted_id)}


@router.get("/")
async def get_notes(user_id=Depends(get_current_user_id)):
    notes = []
    cursor = notes_collection.find({"user_id": user_id}).sort("created_at", -1)

    async for note in cursor:
        notes.append(_to_note_response(note))

    return notes


@router.get("/{note_id}")
async def get_note(note_id: str, user_id=Depends(get_current_user_id)):
    try:
        oid = ObjectId(note_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid note_id")

    note = await notes_collection.find_one({"_id": oid, "user_id": user_id})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return _to_note_response(note)


@router.put("/{note_id}")
async def update_note(note_id: str, note: NoteUpdate, user_id=Depends(get_current_user_id)):
    try:
        oid = ObjectId(note_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid note_id")

    update_data = {k: v for k, v in note.model_dump().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="Nothing to update")

    update_data["updated_at"] = datetime.utcnow()

    result = await notes_collection.update_one(
        {"_id": oid, "user_id": user_id},
        {"$set": update_data},
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Note updated"}


@router.delete("/{note_id}", status_code=200)
async def delete_note(note_id: str, user_id=Depends(get_current_user_id)):
    try:
        oid = ObjectId(note_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid note_id")

    result = await notes_collection.delete_one({"_id": oid, "user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Note deleted"}