from datetime import datetime
from pydantic import BaseModel


class UsageDetailStats(BaseModel):
    start: datetime | None = None
    end: datetime | None = None
    remark: str | None = None
    step: int | None = None
    usage: int


class CountDetailStats(BaseModel):
    start: datetime | None = None
    end: datetime | None = None
    count: int


class TopSubDetailStats(BaseModel):
    username: str
    is_active: bool
    usage: int


class ExpireSubDetailStats(BaseModel):
    username: str
    is_active: bool
    expire: int


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


class AdminStatsResponseNew(BaseModel):
    usage_limit: int | None
    current_usage: int
    left_usage: int | None
    lifetime_usage: int
    current_day_usage: int
    current_week_usage: int
    yesterday_usage: int
    last_week_usage: int
    last_24h_usages: list[UsageDetailStats]
    last_7d_usages: list[UsageDetailStats]
    last_1m_usages: list[UsageDetailStats]
    last_3m_usages: list[UsageDetailStats]
    last_1y_usages: list[UsageDetailStats]
    today_top_10_usage_subscriptions: list[TopSubDetailStats]
    week_top_10_usage_subscriptions: list[TopSubDetailStats]
    month_top_10_usage_subscriptions: list[TopSubDetailStats]
    last_24h_counts: list[CountDetailStats]
    last_7d_counts: list[CountDetailStats]
    last_1m_counts: list[CountDetailStats]
    last_3m_counts: list[CountDetailStats]
    last_1y_counts: list[CountDetailStats]
    limit_count: int
    current_count: int
    left_count: int
    total_subscriptions: int
    active_subscriptions: int
    inactive_subscriptions: int
    disabled_subscriptions: int
    expired_subscriptions: int
    limited_subscriptions: int
    today_new_subscriptions: int
    yesterday_new_subscriptions: int
    today_requested_subscriptions: int
    today_revoked_subscriptions: int
    today_reseted_subscriptions: int
    today_expire_soon_subscriptions: list[ExpireSubDetailStats]
    week_expire_soon_subscriptions: list[ExpireSubDetailStats]
    today_removed_subscriptions: int
    yesterday_removed_subscriptions: int
    total_removed_subscriptions: int
