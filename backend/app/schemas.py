
from pydantic import BaseModel
from typing import Any, List

class ToolResponse(BaseModel):
    tool: str
    data: Any
    sources: List[Any] | None = None
