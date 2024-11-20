from django.contrib import admin
from .models import TipoMascota, Mascota, Evento, Amigos

@admin.register(TipoMascota)
class TipoMascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_nacimiento', 'dueño']
    search_fields = ['nombre']

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_hora', 'ubicacion', 'organizador')
    list_filter = ('fecha_hora',)
    search_fields = ('titulo', 'descripcion', 'ubicacion', 'organizador__username')
    ordering = ('fecha_hora',)
    autocomplete_fields = ('organizador',)

@admin.register(Amigos)
class AmigosAdmin(admin.ModelAdmin):
    list_display = ('id', 'perfil1', 'perfil2', 'fecha_conexion')
    list_filter = ('fecha_conexion',)
    search_fields = ('perfil1__username', 'perfil2__username')
    ordering = ('-fecha_conexion',)
    autocomplete_fields = ('perfil1', 'perfil2')