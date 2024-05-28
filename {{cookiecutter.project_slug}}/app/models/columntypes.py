"""Columnt type overrides for customizations or fixes."""

from sqlalchemy import BigInteger
from sqlalchemy.dialects import mysql
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects import sqlite


AgnosticBigInt = BigInteger()
# SQLAlchemy does not map BigInt to Int by default on the sqlite dialect.
# It should, but it doesn't.
AgnosticBigInt = AgnosticBigInt.with_variant(postgresql.BIGINT(), 'postgresql')
AgnosticBigInt = AgnosticBigInt.with_variant(mysql.BIGINT(), 'mysql')
AgnosticBigInt = AgnosticBigInt.with_variant(sqlite.INTEGER(), 'sqlite')
