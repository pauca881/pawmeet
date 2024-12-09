from django.shortcuts import render

def petadvisorUser(request):
    # Lógica de la vista
    return render(request, 'petadvisor_paraUser.html')

def petadvisorEmpresa(request):
    # Lógica de la vista
    return render(request, 'petadvisor_paraEmpresa.html')
