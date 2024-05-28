import bcrypt


def create(string_to_hash: str) -> str:
    """Hash a string."""
    return bcrypt.hashpw(string_to_hash.encode(), bcrypt.gensalt()).decode()


def compare(first: str, second: str) -> bool:
    """Check if a string matches a hash."""
    return bcrypt.checkpw(first.encode(), second.encode())
