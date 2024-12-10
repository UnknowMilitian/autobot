import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from apps.middlewares import setup_middlewares
from apps.handlers import setup_handlers
from apps.utils.db_manager import db


async def main():
    redis = await Redis.from_url(config.REDIS_URL)

    await db.connect()

    bot = Bot(
        token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=RedisStorage(redis=redis))

    setup_middlewares(dp)

    setup_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    await db.disconnect()
