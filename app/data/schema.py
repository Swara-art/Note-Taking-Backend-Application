from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: str
    
class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteInDB(BaseModel):
    id: str
    title: str
    content: str
    created_at: str
    updated_at: str  
