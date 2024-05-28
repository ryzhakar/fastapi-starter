from datetime import datetime, timedelta, UTC


def get_naive_utcnow() -> datetime:
    """Get the current time in UTC without timezone info."""
    return datetime.now(UTC).replace(tzinfo=None)

def get_validity_window(seconds: int) -> tuple[datetime, datetime]:
    """Get a datetime validity window."""
    now = get_naive_utcnow()
    return now, now + timedelta(seconds=seconds)
