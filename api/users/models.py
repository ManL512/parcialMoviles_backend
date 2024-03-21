#api/users/models.py

from django.db import models

class Usuario(models.Model):
    nombre = models.TextField()
    contrasena = models.TextField()
    token_jwt = models.TextField(blank=True, null=True)
    fecha_expiracion_token = models.DateTimeField(blank=True, null=True)
