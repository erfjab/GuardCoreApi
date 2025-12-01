from datetime import datetime
from pydantic import BaseModel


class UsageDetail(BaseModel):
    start_date: datetime
    end_date: datetime
    usage: int


class UsageSubscriptionDetail(BaseModel):
    username: str
    usage: int
    is_active: bool


class AgentStatsDetail(BaseModel):
    category: str
    count: int


class SubscriptionStatusStatsResponse(BaseModel):
    total: int
    active: int
    disabled: int
    expired: int
    limited: int
    pending: int
    available: int
    unavailable: int
    online: int
    offline: int


class MostUsageSubscription(BaseModel):
    subscriptions: list[UsageSubscriptionDetail]
    start_date: datetime
    end_date: datetime


class UsageStatsResponse(BaseModel):
    total: int
    usages: list[UsageDetail]
    start_date: datetime
    end_date: datetime


class AgentStatsResponse(BaseModel):
    agents: list[AgentStatsDetail]
