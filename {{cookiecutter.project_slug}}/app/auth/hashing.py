import bcrypt


def create(hashable: str) -> str:
    """Hash a string."""
    return bcrypt.hashpw(hashable.encode(), bcrypt.gensalt()).decode()


def compare(hashable: str, hashed: str) -> bool:
    """Check if a string matches a hash."""
    return bcrypt.checkpw(hashable.encode(), hashed.encode())
