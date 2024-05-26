from app.initializers import server
from app.routers import healthcheck
from app.settings import get_settings
from app.initializers import sentry

settings = get_settings()

app = server.get_app(
    healthcheck.router,
    lifespan=server.construct_lifespan(
        pre=[
            sentry.init,
        ],
        post=[],
    ),
)
