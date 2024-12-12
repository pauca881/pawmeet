from django import forms
from mascotas.models import Mascota
from PIL import Image
from dogs_cats_detection.tl_models import predict_image

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
            'tamaño',
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
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '1'}),
            'vacunado': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')], attrs={'class': 'radio-inline'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'nivel_socializacion': forms.Select(attrs={'class': 'form-control'}),
            'tamaño': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if not foto:
            raise forms.ValidationError("Por favor, sube una imagen.")

        try:
            image = Image.open(foto)
            image.verify()  # Verifica si es una imagen válida
        except Exception:
            raise forms.ValidationError("El archivo subido no es una imagen válida.")

        if not predict_image(image):
            raise forms.ValidationError("La imagen no es una mascota válida.")

        return foto

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['castrado'].initial = None
        self.fields['vacunado'].initial = None