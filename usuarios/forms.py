from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError
from datetime import date

# Aquesta classe serveix per que l'usuari tingui almenys 18 anys, en cas contrari, salta un error


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'apellidos', 'direccion',
                  'fecha_nacimiento', 'imagen_perfil']

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')

        today = date.today()
        edad = today.year - fecha_nacimiento.year
        if today.month < fecha_nacimiento.month or (today.month == fecha_nacimiento.month and today.day < fecha_nacimiento.day):
            edad = -1

        if edad < 18:
            raise ValidationError(
                'Debes ser mayor de 18 años para registrarte.')

        return fecha_nacimiento


# python manage.py makemigrations
# python manage.py migrate
