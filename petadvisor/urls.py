from .views import entity_detail
from django.urls import path


patterns = [
    path('entities/<int:entity_id>/', entity_detail, name='entity_detail')
]
