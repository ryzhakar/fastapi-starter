from fastapi import APIRouter, Response


router = APIRouter(
    prefix='/healthcheck',
)


@router.get('/', response_class=Response)
async def healthcheck() -> Response:
    """Try to return a 200 OK response."""
    return Response(status_code=200)
