from django.contrib import admin
from .models import (
    TelegramBotConfiguration,
    User,
    CarBrand,
    CarModel,
    Detection,
    ScrapedCar,
    CeleryTaskLog,
    UserActivity,
    BrandPopularity,
)


@admin.register(TelegramBotConfiguration)
class TelegramBotConfigurationAdmin(admin.ModelAdmin):
    list_display = ("bot_token", "admin")
    fieldsets = (
        ("Bot Settings", {"fields": ("bot_token", "secret_key")}),
        ("Admin Settings", {"fields": ("admin",)}),
    )

    def has_add_permission(self, request):
        # Ensure only one instance exists
        return not TelegramBotConfiguration.objects.exists()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "phone_number",
        "email",
        "is_active",
        "is_staff",
        "created_at",
    )
    list_filter = ("is_active", "is_staff", "language", "date_joined")
    search_fields = ("username", "phone_number", "email")
    ordering = ("-created_at",)


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "popularity_score")
    search_fields = ("name",)
    ordering = ("-popularity_score",)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")
    list_filter = ("brand",)
    search_fields = ("name", "brand__name")
    ordering = ("brand", "name")


@admin.register(Detection)
class DetectionAdmin(admin.ModelAdmin):
    list_display = ("user", "brand", "model", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "brand", "model")
    search_fields = ("user__username", "brand__name", "model__name", "color")
    ordering = ("-created_at",)


@admin.register(ScrapedCar)
class ScrapedCarAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "model", "year", "price", "scraped_at")
    list_filter = ("brand", "model", "year", "scraped_at")
    search_fields = ("title", "brand", "model", "ad_url")
    ordering = ("-scraped_at",)


@admin.register(CeleryTaskLog)
class CeleryTaskLogAdmin(admin.ModelAdmin):
    list_display = ("task_id", "detection", "start_time", "end_time", "status")
    list_filter = ("status", "start_time", "end_time")
    search_fields = ("task_id", "detection__id")
    ordering = ("-start_time",)


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username",)
    ordering = ("user",)


@admin.register(BrandPopularity)
class BrandPopularityAdmin(admin.ModelAdmin):
    list_display = ("brand", "date", "popularity_score")
    list_filter = ("date", "brand")
    search_fields = ("brand__name",)
    ordering = ("-date",)
