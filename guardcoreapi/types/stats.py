from pydantic import BaseModel


class StatsResponse(BaseModel):
    total_subscription: int
    active_subscription: int
    inactive_subscription: int

    hour_usages: int
    today_usages: int
    yesterday_usages: int
    total_usages: int
