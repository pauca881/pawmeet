from django.db import models
from usuarios.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


class PetAdvisor(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        'usuarios.UserProfile', on_delete=models.CASCADE, related_name='reviews')
    professional = models.ForeignKey(
        'usuarios.ProfesionalUser', on_delete=models.CASCADE, related_name='reviews')
    puntuation = models.IntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(5)], help_text='Puntuacuion de 1 a 5 estrellas.')
    description = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('author', 'professional')
        ordering = ['-date']

    def __str__(self):
        return f"Reseña de {self.author} a {self.professional} - {self.puntuation}"
