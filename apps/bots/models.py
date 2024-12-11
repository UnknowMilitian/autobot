from django.db import models


# Create your models here.
class TelegramBotConfiguration(models.Model):
    bot_token = models.CharField(max_length=250)
    secret_key = models.CharField(max_length=250)
    webhook_url = models.URLField(max_length=250)
    admin = models.IntegerField()
