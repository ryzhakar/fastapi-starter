"""User-related models for authorization and authentication.

This data model targets modularity, so it could be adopted for various flows.
Supports any identifiers - emails, usernames, phone numbers, tokens, etc.
Also, it supports various authentication methods. The only implemented one is
password based, but it can be extended with OAuth, OTP, etc.

PLEASE, DON'T SETUP ANY VALIDATION HERE, USE PYDANTIC MODELS INSTEAD.
DATABASE SHOULDN'T KNOW, MUCH LESS CARE ABOUT YOUR BUSINESS LOGIC.
"""

import ulid
from app.models.base import Base
import sqlalchemy as sa
from app.models.columntypes import AgnosticBigInt

_ULID_LENGTH = 26
_BCRYPT_HASH_LENGTH = 60

class User(Base):
    """A user of the application with ULID and soft delete."""

    ulid = sa.Column(
        sa.String(_ULID_LENGTH),
        primary_key=True,
        nullable=False,
        index=True,
        default=lambda: str(ulid.new()),
    )
    identifier = sa.Column(
        sa.String,
        unique=True,
        index=True,
        nullable=False,
        comment='Can be anything: username, email, phone number, etc.',
    )
    is_active = sa.Column(
        sa.Boolean,
        nullable=False,
        default=True,
    )
    refresh_tokens = sa.orm.relationship(
        'RefreshToken',
        back_populates='user',
        cascade='all, delete-orphan',
        passive_deletes=True,
    )

    # AUTHENTICATION
    # Can have 0 or 1 password authentication object
    password_authentication = sa.orm.relationship(
        'PasswordAuthentication',
        back_populates='user',
        uselist=False,
        cascade='all, delete-orphan',
        passive_deletes=True,
    )


class PasswordAuthentication(Base):
    """Password authentication data for the user."""
    user_ulid = sa.Column(
        sa.String(_ULID_LENGTH),
        sa.ForeignKey('user.ulid', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
    )
    hashed_password = sa.Column(
        sa.String(_BCRYPT_HASH_LENGTH),
        nullable=False,
    )
    user = sa.orm.relationship(
        'User',
        back_populates='password_authentication',
    )


class RefreshToken(Base):
    """Refresh token management based on hash.

    Allows to revoke tokens by deactivating them.
    """
    id = sa.Column(
        AgnosticBigInt,
        primary_key=True,
        nullable=False,
    )
    user_ulid = sa.Column(
        sa.String(_ULID_LENGTH),
        sa.ForeignKey('user.ulid', ondelete='CASCADE'),
        nullable=False,
    )
    token_hash = sa.Column(
        sa.String(_BCRYPT_HASH_LENGTH),
        nullable=False,
        unique=True,
    )
    user = sa.orm.relationship(
        'User',
        back_populates='refresh_tokens',
    )
    is_active = sa.Column(
        sa.Boolean,
        nullable=False,
        default=True,
    )
