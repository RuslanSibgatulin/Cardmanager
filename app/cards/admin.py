from django.contrib import admin

from .models import Card, Purchase


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = (
        "number", "series", "release_at", "expiration_at", "status"
    )

    # Поиск по полям
    search_fields = (
        "number", "series", "release_at", "expiration_at", "status"
    )

    # Фильтрация в списке
    list_filter = ("release_at", "expiration_at", "series", "status")


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ("card", "buytime", "amount")

    # Поиск по полям
    search_fields = ("card",)

    # Фильтрация в списке
    list_filter = ("buytime",)
