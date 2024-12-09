# Register your models here.

from django.contrib import admin
from .models import PetAdvisor


@admin.register(PetAdvisor)
class PetAdvisorAdmin(admin.ModelAdmin):
    list_display = ('author', 'professional', 'puntuation', 'date')
    search_fields = ('author__usuario__username',
                     'professional__usuario__username')
    list_filter = ('puntuation', 'date')
    action = ['marcar_como_inapropiado']

    def marcar_como_inapropiado(self, request, queryset):
        queryset.update(comentario='[Reseña marcada como inapropiada]')
        self.message_user(
            request, f"{queryset.count()} reseñas marcadas como inapropiadas.")
    marcar_como_inapropiado.short_description = "Marcar como inapropiado"
