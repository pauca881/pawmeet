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
            'nivel_socializacion'
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
            'nivel_socializacion': 'Nivel de Socialización'
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'castrado': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')],
                                        attrs={'class': 'radio-inline'}),
            'raza': forms.Select(attrs={'class': 'form-control'}),
            'temperamento': forms.Select(attrs={'class': 'form-control'}),
            'nivel_actividad': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'tep': '0.01'}),
            'vacunado': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')],
                                        attrs={'class': 'radio-inline'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'nivel_socializacion': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['castrado'].initial = None
        self.fields['vacunado'].initial = False