from app.initializers import server
from app.routers import healthcheck
from app.settings import get_settings
from app.initializers import sentry

settings = get_settings()
devmode = settings.environment == 'development'

app = server.get_app(
    healthcheck.router,
    lifespan=server.construct_lifespan(
        pre=[
            sentry.init,
        ],
        post=[],
    ),
    docs='/' if devmode else False,
)
