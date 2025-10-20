from typing import List
from pydantic import BaseModel


class ServiceResponse(BaseModel):
    id: int
    remark: str
    node_ids: List[int]

    class Config:
        from_attributes = True


class ServiceCreate(BaseModel):
    remark: str
    node_ids: List[int]


class ServiceUpdate(BaseModel):
    remark: str | None = None
    node_ids: List[int] | None = None
