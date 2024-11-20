from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from usuarios.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['mascota', 'telefono', 'direccion', 'fecha_nacimiento_dueño', 'fecha_nacimiento_mascota', 'foto_persona']

    # Validación personalizada para fecha_nacimiento_dueño
    def clean_fecha_nacimiento_dueño(self):
        fecha_nacimiento_dueño = self.cleaned_data.get('fecha_nacimiento_dueño')

        today = date.today()
        edad = today.year - fecha_nacimiento_dueño.year
        if today.month < fecha_nacimiento_dueño.month or (today.month == fecha_nacimiento_dueño.month and today.day < fecha_nacimiento_dueño.day):
            edad -= 1

        if edad < 18:
            raise ValidationError('Debes ser mayor de 18 años para registrarte.')

        return fecha_nacimiento_dueño
