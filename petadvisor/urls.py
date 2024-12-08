from . import views
from django.urls import path

urlpatterns = [
    path('petadvisor/', views.petadvisor, name='petadvisor')
]