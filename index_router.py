from fastapi import APIRouter

from app.setting.router import router as setting_router

index_router = APIRouter()

index_router.include_router(setting_router)
