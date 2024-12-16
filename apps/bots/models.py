from django.db import models
from solo.models import SingletonModel
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.bots.management import UserManager


# Create your models here.
class TelegramBotConfiguration(SingletonModel):
    bot_token = models.CharField(max_length=250, default="token")
    secret_key = models.CharField(max_length=250, default="secret_key")
    admin = models.IntegerField(default=12345678)


class User(AbstractUser):
    class Preferredlanguage(models.TextChoices):
        UZBEK = "uz", "uz"
        RUSSIAN = "ru", "ru"
        ENGLISH = "en", "en"

    telegram_id = models.BigIntegerField(_("Telegram id"), unique=True, default=0)
    phone_number = models.CharField(max_length=15, unique=True, default="")
    last_activity = models.DateTimeField(auto_now=True)
    total_detections = models.PositiveIntegerField(default=0)

    preferred_language = models.CharField(
        _("Preffered language"),
        max_length=20,
        default=Preferredlanguage.UZBEK,
        choices=Preferredlanguage.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Avoid clash with default User.groups
        blank=True,
        verbose_name=_("Groups"),
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Avoid clash with default User.user_permissions
        blank=True,
        verbose_name=_("User permissions"),
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class CarBrand(models.Model):
    name = models.CharField(_("Car brand"), max_length=100, unique=True)
    popularity_score = models.FloatField(_("Popularity score"), default=0.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car brand"
        verbose_name_plural = "Car brands"


class CarModel(models.Model):
    brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE, related_name="car_models"  # Valid name
    )
    name = models.CharField(_("Name"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car model"
        verbose_name_plural = "Car models"


class Detection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="detection")
    brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE, verbose_name=_("Car brand")
    )
    model = models.ForeignKey(
        CarModel, on_delete=models.CASCADE, verbose_name=_("Model")
    )
    color = models.CharField(_("Color"), max_length=50, blank=True, null=True)
    year_from = models.PositiveIntegerField(blank=True, null=True)
    year_to = models.PositiveIntegerField(blank=True, null=True)
    mileage_from = models.PositiveIntegerField(blank=True, null=True)
    mileage_to = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Detection"
        verbose_name_plural = "Detections"


class ScrapedCar(models.Model):
    detection = models.ForeignKey(
        Detection,
        on_delete=models.CASCADE,
        verbose_name=_("ScrapedCar"),
        related_name="cars",
    )
    title = models.CharField(_("Title"), max_length=100)
    brand = models.CharField(_("Brand"), max_length=100)
    model = models.CharField(_("Model"), max_length=100)
    year = models.IntegerField(_("Year"))
    color = models.CharField(_("Color"), max_length=50)
    mileage = models.IntegerField()
    transmission = models.CharField(
        _("Transmission"), max_length=50, null=True, blank=True
    )
    price = models.DecimalField(_("Price"), max_digits=12, decimal_places=2)
    contact_number = models.CharField(
        _("Contact number"), max_length=15, null=True, blank=True
    )
    ad_url = models.URLField(_("Ad url"))
    images = models.JSONField(_("Images"), default=list)  # List of image URLs
    scraped_at = models.DateTimeField(_("Scraped at"), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Scraped Car"
        verbose_name_plural = "Scraped Cars"


class CeleryTaskLog(models.Model):
    task_id = models.CharField(_("Task id"), max_length=255)
    detection = models.ForeignKey(
        Detection,
        on_delete=models.SET_NULL,
        verbose_name=_("Detection"),
        null=True,
        blank=True,
    )
    start_time = models.DateTimeField(_("Start time"))
    end_time = models.DateTimeField(_("End time"), null=True, blank=True)
    status = models.CharField(
        _("Status"),
        max_length=50,
        choices=[("pending", "Pending"), ("success", "Success"), ("error", "Error")],
    )
    results = models.JSONField(_("Results"), default=dict)

    def __str__(self):
        return self.task_id

    class Meta:
        verbose_name = "Celery task Log"
        verbose_name_plural = "Celery task Logs"


class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="activity")
    interactions_per_day = models.JSONField(
        _("Interactions per day"), default=dict
    )  # {"2024-12-11": 5, "2024-12-10": 3}

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Activity"
        verbose_name_plural = "User Activities"


class BrandPopularity(models.Model):
    brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
        verbose_name=_("Brand popularity"),
        related_name="popularity_stats",
    )
    date = models.DateField(_("Date"))
    popularity_score = models.FloatField(_("Popularity score"))

    def __str__(self):
        return self.brand.name

    class Meta:
        verbose_name = "Brand Popularity"
        verbose_name_plural = "Brand Popularities"
