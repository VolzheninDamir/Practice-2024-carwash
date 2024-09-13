from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Доступ к админке
    path('', include('main.urls')),   # Подключение приложения main
]
