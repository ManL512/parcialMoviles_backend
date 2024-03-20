
# api/models.py
from django.db import models

class Articulo(models.Model):
    imagen = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
