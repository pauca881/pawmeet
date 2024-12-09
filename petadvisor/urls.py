from . import views
from django.urls import path

urlpatterns = [
    path('petadvisor/petadivisorEmpresa', views.petadvisorEmpresa, name='petadvisorEmpresa'),
    path('petadvisor/petadivisorUser', views.petadvisorUser, name='petadvisorUser')
]