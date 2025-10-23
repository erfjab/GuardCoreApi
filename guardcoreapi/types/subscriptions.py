from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class SubscriptionResponse(BaseModel):
    id: int
    username: str
    owner_username: str
    access_key: str

    enabled: bool
    activated: bool
    reached: bool
    limited: bool
    expired: bool
    is_active: bool

    link: str

    limit_usage: int
    reset_usage: int
    total_usage: int
    current_usage: int
    limit_expire: int

    last_reset_at: Optional[datetime]
    last_revoke_at: Optional[datetime]
    last_request_at: Optional[datetime]
    last_client_agent: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SubscriptionCreate(BaseModel):
    username: str
    limit_usage: int
    limit_expire: int


class SubscriptionUpdate(BaseModel):
    limit_usage: Optional[int] = None
    limit_expire: Optional[int] = None


class SubscriptionUsageLog(BaseModel):
    usage: int
    created_at: datetime


class SubscriptionUsageLogsResponse(BaseModel):
    subscription: SubscriptionResponse
    usages: list[SubscriptionUsageLog]


class SubscriptionStatsResponse(BaseModel):
    total: int
    active: int
    inactive: int
    disabled: int
    expired: int
    limited: int
    has_revoked: int
    has_reseted: int
    total_removed: int
    total_usage: int
