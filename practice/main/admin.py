from django.contrib import admin
from .models import Client, Moihik, Zapisi

# Настройка админки для модели Moihik
class MoihikAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']  # Обновите, чтобы использовать актуальные поля

# Настройка админки для модели Client
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

# Настройка админки для модели Zapisi
class ZapisiAdmin(admin.ModelAdmin):
    list_display = ['client', 'moihik', 'date']

# Регистрация моделей в админке
admin.site.register(Client, ClientAdmin)
admin.site.register(Moihik, MoihikAdmin)
admin.site.register(Zapisi, ZapisiAdmin)
