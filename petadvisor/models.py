from django.db import models as m
from usuarios.models import UserProfile


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

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum(review.rating for review in reviews) / reviews.count()
        return 0


class Reviews(m.Model):
    # Cada classe representa una resenya d'usuaria sobre qualsevol tipus de PetEntity
    user = m.ForeignKey(UserProfile, on_delete=m.Case)
    pet_entity = m.ForeignKey(
        PetEntity, related_name='reviews', on_delete=m.CASCADE)
    rating = m.PositiveSmallIntegerField(null=False)
    comment = m.TextField(blank=True, null=True)
    created_at = m.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.usuario} on {self.pet_entity.name}"

    class Meta:
        # Fem que un usuari tingui la capacitat nomes de crear una review per cada entity_type.
        constraints = [
            m.UniqueConstraint(
                fields=['user', 'pet_entity'], name='unique_review_per_user_and_entity')
        ]
        ordering = ['-created_at']


# python manage.py makemigrations
# python manage.py migrate
