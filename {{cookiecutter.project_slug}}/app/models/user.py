import ulid
from app.models.base import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String


class User(Base):
    """A user of the application with ULID and soft delete."""

    ulid = Column(
        String,
        primary_key=True,
        nullable=False,
        index=True,
        default=lambda: str(ulid.new()),
    )
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
