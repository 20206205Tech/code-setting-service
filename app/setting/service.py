from sqlalchemy.orm import Session

from app.setting.schema import UpsertSettingsRequest
from database.models import UserSetting


def get_user_settings(db: Session, user_id: str):
    return db.query(UserSetting).filter(UserSetting.user_id == user_id).all()


def upsert_user_settings(db: Session, user_id: str, request: UpsertSettingsRequest):
    existing_settings = (
        db.query(UserSetting).filter(UserSetting.user_id == user_id).all()
    )

    existing_map = {setting.key: setting for setting in existing_settings}

    for item in request.settings:
        if item.key in existing_map:
            existing_map[item.key].value = item.value
        else:
            new_setting = UserSetting(user_id=user_id, key=item.key, value=item.value)
            db.add(new_setting)

    db.commit()
    return True
