import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.api.v0.api import router as api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world - welcome to Dewaffle"}


def start():
    """Launch from root folder on local host."""
    uvicorn.run("app.main:app")


def start_docker():
    """Use for running inside container to access incoming requests."""
    uvicorn.run("app.main:app", host="0.0.0.0")


app.include_router(api_router, prefix="/api/v0")
handler = Mangum(app)
