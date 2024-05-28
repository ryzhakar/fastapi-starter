import jwt
from app.settings import get_settings
from app.utilities.datetime import get_validity_window

_SECRET_KEY = get_settings().secret_key.get_secret_value()


def issue(ulid: str, *, expires_in_seconds: int) -> str:
    """Encode the user's ULID into a JWT."""
    iat, exp = get_validity_window(expires_in_seconds)
    payload = {
        'sub': ulid,
        'iat': iat,
        'exp': exp,
    }
    return jwt.encode(payload, _SECRET_KEY, algorithm='HS256')


def verify(token: str) -> str:
    """Decode the user's ULID from a JWT.

    Warning: you probably want to catch jwt.ExpiredSignatureError.
    """
    return jwt.decode(token, _SECRET_KEY, algorithms=['HS256'])['sub']
