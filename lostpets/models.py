from django.db import models
from usuarios.models import UserProfile
from mascotas.models import Mascota
from django.utils.timezone import now

# Create your models here.


class LostPet(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='lost_pet')
    pet = models.ForeignKey(
        Mascota, on_delete=models.CASCADE, related_name='lost_reports')
    location = models.TextField(
        help_text='Lugar aproximado donde se perdio la mascota.')
    date_lost = models.DateTimeField(
        help_text='Hora aproximada en que se perdio la mascota.')
    description = models.TextField(
        help_text='Detalles adicionales', null=True, blank=True)
    is_found = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet.nombre} - Perdido en {self.location} ({'Encontrado' if self.is_found else 'No encontrado'})"

    def mark_as_found(self):
        self.is_found = True
        self.found_date = now()
        self.save()
        pass
