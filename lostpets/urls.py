from django.urls import path
from . import views

app_name = 'lostpets'

urlpatterns = [
    path('report/', views.report_lost_pet, name='report'),
]
