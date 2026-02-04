from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI

from routes.create import router as create_router
from routes.read import router as read_router
from routes.update import router as update_router

app = FastAPI()

app.include_router(create_router)
app.include_router(read_router)
app.include_router(update_router)

@app.get("/health")
async def read_root():
    return {"status": "ok"}

