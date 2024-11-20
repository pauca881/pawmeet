from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LostPet
from .forms import LostPetForm

# Create your views here.


@login_required
def report_lost_pet(request):
    if request.method == 'POST':
        form = LostPetForm(request.POST)
        if form.is_valid():
            lost_pet = form.save(commit=False)
            lost_pet.user = request.user
            lost_pet.save()
            return redirect('lostpets:list')
    else:
        form = LostPetForm()
    return render(request, 'lostpets/report_lost_pet.html', {'form': form})
