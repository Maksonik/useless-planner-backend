from datetime import datetime

from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str = Field(max_length=255)
    description: str = Field(max_length=500)
    done: bool = Field(default=False)
    deadline: datetime

