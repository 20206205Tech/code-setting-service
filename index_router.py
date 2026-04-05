from app.admin.router import router as admin_persona_router
from app.public.router import router as public_persona_router
from fastapi import APIRouter

index_router = APIRouter()

index_router.include_router(public_persona_router)
index_router.include_router(admin_persona_router)
