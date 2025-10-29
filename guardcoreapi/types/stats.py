from datetime import datetime
from pydantic import BaseModel


class UsageDetailStats(BaseModel):
    start: datetime | None = None
    end: datetime | None = None
    remark: str | None = None
    usage: int


class StatsResponse(BaseModel):
    total_subscriptions: int
    active_subscriptions: int
    inactive_subscriptions: int
    online_subscriptions: int
    most_usage_subscription: str | None = None
    most_usage_subscriptions: list[UsageDetailStats]

    total_admins: int
    active_admins: int
    inactive_admins: int
    most_usage_admins: list[UsageDetailStats]

    total_nodes: int
    active_nodes: int
    inactive_nodes: int
    most_usage_nodes: list[UsageDetailStats]

    total_lifetime_usages: int
    total_day_usages: int
    total_week_usages: int
    last_24h_usages: list[UsageDetailStats]
    last_7d_usages: list[UsageDetailStats]
