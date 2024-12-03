from django.shortcuts import render
from usuarios.models import UserProfile  # Importamos el modelo UserProfile

def list_user_profiles(request):
    user_profiles = UserProfile.objects.all()  # Recupera todos los perfiles
    return render(request, 'meetup/user_profile_list.html', {'user_profiles': user_profiles})
