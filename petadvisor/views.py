from django.shortcuts import render, get_object_or_404
from .models import PetEntity

def petadvisor(request):
    # Lógica de la vista
    return render(request, 'petadvisor.html')