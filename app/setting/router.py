from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user_id
from common.response.base_response import BaseResponse
from database.config import get_db

from . import schema, service

router = APIRouter(prefix="/settings", tags=["User Settings"])


@router.get("", response_model=BaseResponse[List[schema.SettingItem]])
def get_settings(
    user_id: str = Depends(get_current_user_id), db: Session = Depends(get_db)
):
    data = service.get_user_settings(db, user_id)
    return BaseResponse(success=True, message="Lấy cài đặt thành công", data=data)


@router.post("", response_model=BaseResponse)
def upsert_settings(
    request: schema.UpsertSettingsRequest,
    user_id: str = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    service.upsert_user_settings(db, user_id, request)
    return BaseResponse(success=True, message="Cập nhật cài đặt thành công")
