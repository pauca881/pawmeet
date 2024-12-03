from . import views
from django.urls import path


patterns = [
    path('', views.petadvisor, name='petadvisor.html')
]
