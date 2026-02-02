from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from routes.create import router

app = FastAPI()

app.include_router(router)

@app.get("/health")
async def read_root():
    return {"status": "ok"}

