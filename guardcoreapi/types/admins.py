from enum import StrEnum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class AdminPlaceHolderCategory(StrEnum):
    INFO = "info"
    LIMITED = "limited"
    EXPIRED = "expired"
    DISABLED = "disabled"


ADMIN_PLACEHOLDER_REMARK_FORMATS = [
    "id",
    "username",
    "owner_username",
    "enabled",
    "activated",
    "limited",
    "expired",
    "is_active",
    "limit_usage",
    "current_usage",
    "left_usage",
    "expire_date",
    "expire_in",
    "expire_in_days",
]


class AdminPlaceHolder(BaseModel):
    remark: str
    categories: list[AdminPlaceHolderCategory]


class AdminRole(StrEnum):
    OWNER = "owner"
    RESELLER = "reseller"


class AdminToken(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AdminResponse(BaseModel):
    id: int
    enabled: bool
    removed: bool
    username: str
    role: AdminRole
    service_ids: list[int]
    create_access: Optional[bool]
    update_access: Optional[bool]
    remove_access: Optional[bool]
    count_limit: Optional[int]
    current_count: Optional[int]
    left_count: Optional[int]
    reached_count_limit: Optional[bool]
    usage_limit: Optional[int]
    current_usage: Optional[int]
    left_usage: Optional[int]
    reached_usage_limit: Optional[bool]
    placeholders: Optional[list[AdminPlaceHolder]]
    max_links: Optional[int]
    shuffle_links: Optional[bool]
    api_key: str
    last_login_at: Optional[datetime]
    last_online_at: Optional[datetime]
    access_title: Optional[str] = None
    access_description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AdminCreate(BaseModel):
    username: str
    password: str
    role: AdminRole
    service_ids: Optional[list[int]]
    create_access: Optional[bool] = False
    update_access: Optional[bool] = False
    remove_access: Optional[bool] = False
    count_limit: Optional[int] = None
    usage_limit: Optional[int] = None
    access_prefix: Optional[str] = None


class AdminUpdate(BaseModel):
    password: Optional[str] = None
    create_access: Optional[bool] = None
    update_access: Optional[bool] = None
    remove_access: Optional[bool] = None
    count_limit: Optional[int] = None
    usage_limit: Optional[int] = None
    service_ids: Optional[list[int]] = None
    placeholders: Optional[list[AdminPlaceHolder]] = None
    max_links: Optional[int] = None
    shuffle_links: Optional[bool] = None
    access_prefix: Optional[str] = None


class AdminCurrentUpdate(BaseModel):
    password: Optional[str] = None
    placeholders: Optional[list[AdminPlaceHolder]] = None
    max_links: Optional[int] = None
    shuffle_links: Optional[bool] = None


class AdminUsageLog(BaseModel):
    usage: int
    created_at: datetime


class AdminUsageLogsResponse(BaseModel):
    admin: AdminResponse
    usages: list[AdminUsageLog]
