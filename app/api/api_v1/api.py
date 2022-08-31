from fastapi import APIRouter

from .endpoints import todo

router = APIRouter()
router.include_router(todo.router, prefix="/todo", tags=["Todo"])