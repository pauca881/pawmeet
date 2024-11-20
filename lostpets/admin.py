from django.contrib import admin
from .models import LostPet
# Register your models here.


@admin.register(LostPet)
class LostPetAdmin(admin.ModelAdmin):
    list_display = ('pet', 'user', 'location', 'date_lost', 'is_found')
    list_filter = ('is_found', 'date_lost')
    search_fields = ('pet__name', 'user__username', 'location')
