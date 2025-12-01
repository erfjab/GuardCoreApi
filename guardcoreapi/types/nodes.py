from enum import StrEnum
from datetime import datetime
from pydantic import BaseModel


class NodeCategory(StrEnum):
    marzban = "marzban"
    marzneshin = "marzneshin"


class NodeResponse(BaseModel):
    id: int
    enabled: bool
    remark: str
    category: NodeCategory
    username: str
    password: str
    host: str
    current_usage: int
    last_used_at: datetime | None
    usage_rate: float | None
    offset_link: int
    batch_size: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NodeCreate(BaseModel):
    remark: str
    category: NodeCategory
    username: str
    password: str
    host: str
    offset_link: int = 0
    batch_size: int = 1
    usage_rate: float = 1.0


class NodeUpdate(BaseModel):
    remark: str | None = None
    username: str | None = None
    password: str | None = None
    host: str | None = None
    offset_link: int | None = None
    batch_size: int | None = None
    usage_rate: float | None = None


class NodeStatsResponse(BaseModel):
    total_nodes: int
    active_nodes: int
    inactive_nodes: int

    class Config:
        from_attributes = True
