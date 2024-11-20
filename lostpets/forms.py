from django import forms
from .models import LostPet


class LostPetForm(forms.ModelForm):
    class Meta:
        model = LostPet
        fields = ['pet', 'location', 'date_lost', 'description']
        widgets = {
            'date_lost': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'pet': 'Mascota',
            'location': 'Ubicación',
            'date_lost': 'Fecha y hora perdida',
            'description': 'Descripción',
        }
