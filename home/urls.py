from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('conectar/', views.conectar_view, name='conectar'),
    path('meetups/', views.eventos_view, name='eventos'),
    path('unirme_a_evento/', views.unirme_a_evento, name='unirme_a_evento'),
]
