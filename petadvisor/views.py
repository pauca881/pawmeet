from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import PetEntity


def petadvisor(request, entity_id):
    entity = get_object_or_404(PetEntity, id=entity_id)
    reviews = entity.reviews.all()
    return render(request, 'petadvisor.html', {'entity': entity, 'reviews': reviews})
