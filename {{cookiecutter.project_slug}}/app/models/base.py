from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func
from app.utilities.naming import to_table_name


class Base(AsyncAttrs, DeclarativeBase):
    """Base model class with timestamps."""

    @declared_attr
    def __tablename__(cls) -> str:  # noqa: N805
        """Use pluralized class name as the table name."""
        return to_table_name(cls.__name__)

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
