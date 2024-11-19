from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mascotas(request):
    return HttpResponse("Estas son las vistas de mascotas")

