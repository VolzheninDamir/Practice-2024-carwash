from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('clients/change/<int:id>/', views.clients_change, name='clients_change'),  # Маршрут принимает ID
    path('moihiki/', views.moihiki, name='moihiki'),
    path('moihiki/change/<int:id>/', views.moihiki_change, name='moihiki_change'),
    path('zapisi/', views.zapisi, name='zapisi'),
    path('zapisi/change/<int:id>/', views.zapisi_change, name='zapisi_change'),
]
