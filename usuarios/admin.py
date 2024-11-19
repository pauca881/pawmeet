from django.contrib import admin
from usuarios.models import UserProfile, TipoProfesional, ProfesionalUser, Reseña
from django.contrib.auth.models import User

@admin.register(User)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'correo', 'fecha_registro')
    search_fields = ('nombre', 'apellidos', 'correo')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'direccion', 'fecha_nacimiento_dueño')

    search_fields = ('usuario__nombre', 'usuario__apellidos', 'telefono')

    search_fields = ('usuarionombre', 'usuarioapellidos', 'telefono')



@admin.register(TipoProfesional)
class TipoProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(ProfesionalUser)
class ProfesionalUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre_establecimiento', 'tipo_de_profesional', 'telefono')

    search_fields = ('usuario__nombre', 'usuario__apellidos', 'nombre_establecimiento', 'telefono')

    search_fields = ('usuarionombre', 'usuarioapellidos', 'nombre_establecimiento', 'telefono')


@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('id', 'profesional', 'numero_estrellas', 'titulo')
    search_fields = ('titulo', 'profesional__nombre_establecimiento')