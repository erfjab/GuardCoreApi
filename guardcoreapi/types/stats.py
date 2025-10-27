from datetime import datetime
from pydantic import BaseModel


class UsageStats(BaseModel):
    start: datetime
    end: datetime
    usage: int


class StatsResponse(BaseModel):
    total_subscription: int
    active_subscription: int
    inactive_subscription: int
    last_24_hours: list[UsageStats]
    today_usage: int
    last_7_days: list[UsageStats]
    week_usage: int
    total_usage: int
