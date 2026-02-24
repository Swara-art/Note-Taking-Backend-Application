from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.notes import router as notes_router

app = FastAPI(title="Note Taking Backend")

app.include_router(auth_router)
app.include_router(notes_router)

@app.get("/health")
def health():
    return {"status": "ok"}