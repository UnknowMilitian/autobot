import json
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Ваш импорт для бота, если требуется
from apps.bots.config.bot import dp
from apps.bots.models import TelegramBotConfiguration

from aiogram import Bot, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode


# Применяем декоратор @csrf_exempt к методу POST
class TelegramWebhook(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        telegram_conf = TelegramBotConfiguration.get_solo()
        bot = Bot(
            token=telegram_conf.bot_token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )

        try:
            data = json.loads(request.body)
            print(data)
            async_to_sync(dp.feed_update)(bot=bot, update=types.Update(**data)) # Added async to sync
        except json.JSONDecodeError:
            print("error")
            return HttpResponse("Invalid JSON", status=400)

        return HttpResponse("Webhook updated successfully !")
