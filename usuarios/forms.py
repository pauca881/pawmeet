from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from usuarios.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
        help_texts = {
            'username': '',  # Elimina el texto de ayuda del campo username
        }

class UserProfileCreationForm(forms.ModelForm):
    telefono = forms.CharField(
        max_length=9,
        min_length=9,
        label='Teléfono',
        widget=forms.TextInput(attrs={
            'type': 'tel',  # Cambia el tipo a 'tel' para permitir solo números
            'pattern': '[0-9]*', 
            'title': 'Solo números', 
            'maxlength': '9'
        }),
        required=True  # Campo obligatorio
    )
    
    # Campo dirección como un campo de texto simple
    direccion = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingresa tu dirección completa',  # Mensaje de ayuda
            'maxlength': '255'  # Limitar la longitud de la dirección
        }),
        required=True  # Campo obligatorio
    )
    
    fecha_nacimiento_dueño = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True  # Campo obligatorio
    )

    class Meta:
        model = UserProfile
        fields = ['fecha_nacimiento_dueño', 'telefono', 'direccion']

    # Validación personalizada para el campo telefono
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if telefono:
            if len(telefono) != 9:
                raise ValidationError('El teléfono debe tener exactamente 9 dígitos.')

        return telefono

    # Validación personalizada para fecha_nacimiento_dueño
    def clean_fecha_nacimiento_dueño(self):
        fecha_nacimiento_dueño = self.cleaned_data.get('fecha_nacimiento_dueño')

        if fecha_nacimiento_dueño:
            today = date.today()
            edad = today.year - fecha_nacimiento_dueño.year
            if today.month < fecha_nacimiento_dueño.month or (
                today.month == fecha_nacimiento_dueño.month and today.day < fecha_nacimiento_dueño.day
            ):
                edad -= 1

            if edad < 18:
                raise ValidationError('Debes ser mayor de 18 años para registrarte.')

        return fecha_nacimiento_dueño