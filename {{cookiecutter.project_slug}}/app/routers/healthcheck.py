from fastapi import APIRouter


router = APIRouter()


@router.get('/healthcheck')
async def healthcheck() -> dict:
    """Try to return a 200 OK response."""
    return {'status': 'ok'}
