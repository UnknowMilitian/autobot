from .commands import router as commands_router
from .registration import router as registration_router


def setup_handlers(dp):
    dp.include_router(commands_router)
    dp.include_router(registration_router)
