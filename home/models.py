from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    username = models.CharField(max_length=150, unique=True)  # Campo username único
    email = models.EmailField(unique=True)  # Campo email único
    password = models.CharField(max_length=255)  # Campo para almacenar la contraseña

    def __str__(self):
        return self.username
