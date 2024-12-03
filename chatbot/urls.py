from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.chatbot_response, name='chatbot_response'),
    path('', views.chatbot_interface, name='chatbot_interface'),
]
