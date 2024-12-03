
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.list_user_profiles, name='list_user_profiles'),
]