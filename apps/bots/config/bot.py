from apps.bots.config import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from apps.bots.middlewares import setup_middlewares
from apps.bots.handlers import setup_handlers


redis = Redis.from_url(config.REDIS_URL)

# bot = Bot(
#     token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
# )
dp = Dispatcher(storage=RedisStorage(redis=redis))

setup_middlewares(dp)

setup_handlers(dp)
