from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func


class Base(AsyncAttrs, DeclarativeBase):
    """Base model class with timestamps."""

    @declared_attr
    def __tablename__(cls) -> str:  # noqa: N805
        """Use pluralized class name as the table name."""
        lowercased = cls.__name__.lower()
        return f'{lowercased}s'

    created = Column(
        DateTime(timezone=False),
        default=func.now(),
        index=True,
    )
    updated = Column(
        DateTime(timezone=False),
        default=func.now(),
        onupdate=func.now(),
    )
