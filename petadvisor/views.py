from django.shortcuts import render, get_object_or_404
from .models import PetAdvisor

def petadvisorUser(request):
    # Lógica de la vista
    return render(request, 'petadvisor_paraUser.html')

def petadvisorEmpresa(request):
    # Lógica de la vista
    return render(request, 'petadvisor_paraEmpresa.html')
