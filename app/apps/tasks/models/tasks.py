from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.integrations.database.base import BaseModel


class Tasks(BaseModel):
    __tablename__ = "tasks"

    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, title={self.title!r}"