from django.contrib import admin
from .models import TipoMascota, Mascota, Evento, Amigos


@admin.register(TipoMascota)
class TipoMascotaAdmin(admin.ModelAdmin):
    """
    Configuración del modelo TipoMascota en el panel de administración.
    """
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    """
    Configuración del modelo Mascota en el panel de administración.
    """
    list_display = ('id', 'nombre', 'edad', 'tipo_mascota', 'dueño')
    list_filter = ('tipo_mascota', 'edad')
    search_fields = ('nombre', 'dueño__username', 'tipo_mascota__nombre')
    ordering = ('nombre',)
    autocomplete_fields = ('tipo_mascota', 'dueño')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    """
    Configuración del modelo Evento en el panel de administración.
    """
    list_display = ('id', 'titulo', 'fecha_hora', 'ubicacion', 'organizador')
    list_filter = ('fecha_hora',)
    search_fields = ('titulo', 'descripcion', 'ubicacion', 'organizador__username')
    ordering = ('fecha_hora',)
    autocomplete_fields = ('organizador',)


@admin.register(Amigos)
class AmigosAdmin(admin.ModelAdmin):
    """
    Configuración del modelo Amigos en el panel de administración.
    """
    list_display = ('id', 'perfil1', 'perfil2', 'fecha_conexion')
    list_filter = ('fecha_conexion',)
    search_fields = ('perfil1__username', 'perfil2__username')
    ordering = ('-fecha_conexion',)
    autocomplete_fields = ('perfil1', 'perfil2')