from pydantic import BaseModel
from typing import Optional


class LogsBase(BaseModel):
    pass


class LogsRequest(LogsBase):
    pass


class LogsResponse(LogsBase):
    message: str
