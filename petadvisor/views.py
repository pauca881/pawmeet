from django.shortcuts import render, get_object_or_404
from .models import PetAdvisor


def petadvisor(request):
    # Lógica de la vista
    return render(request, 'petadvisor.html')
