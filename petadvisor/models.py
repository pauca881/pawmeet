from django.db import models as m
from usuarios import models as mu

# Create your models here.


class PetEntity(m.Model):

    # Classe de python on apereixen tot els tipus de llocs possibles per a gossos.
    entity_type = [('veterinary, Veterinary'),
                   ('pet store', 'Pet Store'),
                   ('dog park', 'Dog Park')
                   ]

    name = m.CharField(max_length=255)
    entity_type = m.CharField(max_length=50, choices=entity_type)
    adress = m.TextField()
    description = m.TextField(null=True, blank=True)
    created_at = m.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_entity_type_display()})"


class Reviews(m.Model):
    # Cada classe representa una resenya d'usuaria sobre qualsevol tipus de PetEntity
    user = m.ForeignKey(mu.Usuario, on_delete=m.Case)


class Review(models.Model):
    """
    Representa una reseña de un usuario sobre un PetEntity.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_entity = models.ForeignKey(
        PetEntity, related_name='reviews', on_delete=models.CASCADE)
    # Calificación, por ejemplo, de 1 a 5
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.pet_entity.name}"

    class Meta:
        # Un usuario solo puede reseñar una entidad una vez.
        unique_together = ('user', 'pet_entity')
        ordering = ['-created_at']
