from django import forms
from mascotas.models import Mascota

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
            'tamaño',  # Agregar el campo tamaño a la lista de fields
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
    
    # Esta funcion sirve para manejar errores en caso que la foto subida no sea valida, en caso de que no lo sea, se informa al usuario. 
    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        from PIL import Image
        from dogs_cats_detection.tl_models import predict_image

        image = Image.open(foto)
        if not predict_image(image):
            raise forms.ValidationError("La imagen no es una mascota valida.")
        return foto

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['castrado'].initial = None
        self.fields['vacunado'].initial = None