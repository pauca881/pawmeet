from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import PetEntity, Reviews


@admin.register(PetEntity)
class PetEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'entity_type', 'average_rating', 'created_at')
    search_fields = ('name', 'entity_type', 'address')


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet_entity', 'rating', 'created_at')
    search_fields = ('user__username', 'pet_entity__name', 'comment')
    list_filter = ('rating', 'created_at')
