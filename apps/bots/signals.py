import requests
from django.dispatch import receiver
from django.db.models.signals import pre_save

from apps.bots.models import TelegramBotConfiguration