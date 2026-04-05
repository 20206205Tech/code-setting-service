from typing import List

from pydantic import BaseModel


class SettingItem(BaseModel):
    key: str
    value: str


class UpsertSettingsRequest(BaseModel):
    settings: List[SettingItem]
