from django import forms
from .models import Mascota
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

import logging

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'fecha_nacimiento',
            'foto',
            'castrado',
            'raza',
            'temperamento',
            'nivel_actividad',
            'peso',
            'vacunado',
            'color',
            'nivel_socializacion',
            'tamaño'
        ]

        labels = {
            'nombre': 'Nombre de la Mascota',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'foto': 'Foto',
            'castrado': 'Castrado',
            'raza': 'Selecciona la raza',
            'temperamento': 'Temperamento',
            'nivel_actividad': 'Nivel de Actividad',
            'peso': 'Peso (kg)',
            'vacunado': 'Vacunado',
            'color': 'Color',
            'nivel_socializacion': 'Nivel de Socialización',
            'tamaño': 'Tamaño',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'castrado': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')], attrs={'class': 'radio-inline'}),
            'raza': forms.Select(attrs={'class': 'form-control'}),
            'temperamento': forms.Select(attrs={'class': 'form-control'}),
            'nivel_actividad': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '1'}),  # Solo permite enteros, sin decimales
            'vacunado': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')], attrs={'class': 'radio-inline'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'nivel_socializacion': forms.Select(attrs={'class': 'form-control'}),
            'tamaño': forms.Select(attrs={'class': 'form-control'}),
        }


    def clean_foto(self):

        foto = self.cleaned_data.get('foto')
        if foto:  # Check if a file was uploaded
            try:
                image = Image.open(foto)
                # You can add further image validation here if needed (e.g., size, format)
                # Convert the image to webp format
                if image.format != 'WEBP':
                    buffer = BytesIO()
                    image.save(buffer, format='WEBP')
                    webp_image = ContentFile(buffer.getvalue(), name=foto.name.split('.')[0] + '.webp')
                    return webp_image
                return foto
            except Exception as e:
                raise forms.ValidationError(f"Error processing image: {e}")
        else:
            return None  # Return None if no file was uploaded

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['castrado'].initial = None
        self.fields['vacunado'].initial = None