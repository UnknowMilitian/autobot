import json
from asgiref.sync import async_to_sync
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Ваш импорт для бота, если требуется
from apps.bots.config.bot import dp
from apps.bots.models import TelegramBotConfiguration

from aiogram import Bot, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
