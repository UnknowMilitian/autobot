import asyncio
import logging
from loguru import logger
from bot import main as run_bot


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.create_task(run_bot())
        event_loop.run_forever()
    except KeyboardInterrupt:
        logger.info("Bot stopped !")
