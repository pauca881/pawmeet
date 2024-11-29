from django import forms
from mascotas.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'fecha_nacimiento', 'foto', 'castrado']
        labels = {
            'nombre': 'Nombre de la Mascota',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'foto': 'Foto',
            'castrado': 'Castrado',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'castrado': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')],
                                        attrs={'class': 'radio-inline'}),
        }

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['castrado'].initial = None
