from django.db import models
from solo.models import SingletonModel


# Create your models here.
class TelegramBotConfiguration(SingletonModel):
    bot_token = models.CharField(max_length=250, default="token")
    secret_key = models.CharField(max_length=250, default="secret_key")
    webhook_url = models.URLField(max_length=250, default="https://api.telegram.org/")
    admin = models.IntegerField(default=12345678)
