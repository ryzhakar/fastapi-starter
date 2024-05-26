from sqlalchemy import BigInteger
from sqlalchemy.dialects import mysql
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects import sqlite


BigIntegerType = BigInteger()
# SQLAlchemy does not map BigInt to Int by default on the sqlite dialect.
# It should, but it doesnt.
BigIntegerType = BigIntegerType.with_variant(postgresql.BIGINT(), 'postgresql')
BigIntegerType = BigIntegerType.with_variant(mysql.BIGINT(), 'mysql')
BigIntegerType = BigIntegerType.with_variant(sqlite.INTEGER(), 'sqlite')
