from django.shortcuts import render
from django.http import HttpResponse

# Our views
def home_view(request):
    return render(request, 'home.html')

def conectar_view(request):
    return render(request, 'conectar.html')