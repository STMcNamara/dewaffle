import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.api.v0.api import router as api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world - welcome to Dewaffle"}


def start():
    """Launch from root folder"""
    uvicorn.run("app.main:app")


app.include_router(api_router, prefix="/api/v0")
handler = Mangum(app)
