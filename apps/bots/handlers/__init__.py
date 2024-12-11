from .commands import router as commands_router


def setup_handlers(dp):
    dp.include_router(commands_router)
