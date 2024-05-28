from fastapi import APIRouter
import ulid
from app import auth

router = APIRouter()


@router.get('/healthcheck')
async def healthcheck() -> dict:
    """Try to return a 200 OK response."""
    user_ulid = str(ulid.new().str)
    jwt = auth.ulidjwt.issue(user_ulid, expires_in_seconds=60)
    jwt_hash_1 = auth.hashing.create(jwt)
    return {
        'ulid_matches': user_ulid == auth.ulidjwt.verify(jwt),
        'jwt_hashes_match': auth.hashing.compare(jwt, jwt_hash_1),
        'ulid': user_ulid,
        'jwt': jwt,
        'jwt_hash_1': jwt_hash_1,
    }
