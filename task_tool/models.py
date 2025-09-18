from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    priority: str = Field("medium", pattern="^(low|medium|high)$")
    done: bool = False
