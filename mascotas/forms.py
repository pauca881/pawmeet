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

    def clean_foto(self):

        foto = self.cleaned_data.get('foto')
        logging.critical("clean_foto")
        if foto:  # Check if a file was uploaded
            logging.critical("clean_foto2")
            try:
                image = Image.open(foto)
                # You can add further image validation here if needed (e.g., size, format)
                # Convert the image to webp format
                logging.critical("clean_foto")
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