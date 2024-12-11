import json
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Ваш импорт для бота, если требуется
from apps.bots.config.bot import dp
from apps.bots.models import TelegramBotConfiguration
from aiogram import Bot


# Применяем декоратор @csrf_exempt к методу POST
class TelegramWebhook(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):

        bot = Bot(
            token=config.BOT_TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )

        try:
            data = json.loads(request.body)
            print(data)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)

        return HttpResponse("Webhook updated successfully !")
