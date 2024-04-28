from fastapi import APIRouter

from .endpoints import recipies

router = APIRouter()
router.include_router(recipies.router, prefix="/recipies", tags=["Recipies"])