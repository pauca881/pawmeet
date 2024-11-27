from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from usuarios.models import UserProfile, Mascota  # Asegúrate de tener un modelo Mascota
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

    # Validación personalizada para el campo username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este nombre de usuario ya está en uso. Por favor elige otro.')

        return username

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

            # Verificar si el número de teléfono ya existe en la base de datos
            if UserProfile.objects.filter(telefono=telefono).exists():
                raise ValidationError("Este número de teléfono ya está en uso.")

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


# Nuevos formularios para ajustes de perfil
class UserProfileSettingsForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', max_length=30, required=True)
    apellidos = forms.CharField(label='Apellidos', max_length=30, required=True)
    email = forms.EmailField(label='Email', required=True)
    telefono = forms.CharField(
        max_length=9,
        min_length=9,
        label='Teléfono',
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'pattern': '[0-9]*',
            'title': 'Solo números',
            'maxlength': '9'
        }),
        required=True
    )
    calle = forms.CharField(
        label='Calle',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingresa tu calle completa',
            'maxlength': '255'
        }),
        required=True
    )
    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={
            'placeholder': 'Ingresa una descripción sobre ti',
            'maxlength': '500'
        }),
        required=False
    )

    class Meta:
        model = UserProfile
        fields = ['nombre', 'apellidos', 'email', 'telefono', 'calle', 'descripcion']

    # Validación personalizada para el campo telefono
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            if len(telefono) != 9:
                raise ValidationError('El teléfono debe tener exactamente 9 dígitos.')
            # Verificar si el número de teléfono ya existe en la base de datos
            if UserProfile.objects.filter(telefono=telefono).exists():
                raise ValidationError("Este número de teléfono ya está en uso.")
        return telefono


class MascotaForm(forms.ModelForm):
    nombre_mascota = forms.CharField(label='Nombre de la Mascota', max_length=30, required=True)
    tipo_mascota = forms.ChoiceField(choices=[('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')], label='Tipo de Mascota', required=True)
    foto_mascota = forms.ImageField(label='Foto de la Mascota', required=False)

    class Meta:
        model = Mascota  # Asegúrate de tener un modelo Mascota
        fields = ['nombre_mascota', 'tipo_mascota', 'foto_mascota']


class UserPasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Contraseña Actual', required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, label='Nueva Contraseña', required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar Nueva Contraseña', required=True)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


class DeleteMascotaForm(forms.Form):
    mascota_id = forms.IntegerField(widget=forms.HiddenInput)

    def clean_mascota_id(self):
        mascota_id = self.cleaned_data.get('mascota_id')
        # Aquí puedes agregar lógica para verificar si el usuario tiene más de una mascota
        # Si solo tiene una mascota, lanza una excepción
        if Mascota.objects.filter(user=self.user, id=mascota_id).count() <= 1:
            raise ValidationError("No puedes borrar la última mascota.")
        return mascota_id