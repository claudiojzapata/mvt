from django.db import models

# Create your models here.
class familiar(models.Model):
    nombre = models.CharField(max_length=30),
    edad = models.CharField(max_length=10),
    esta_activo = models.BooleanField(default=True),
    parentesco = models.CharField(max_length=30),