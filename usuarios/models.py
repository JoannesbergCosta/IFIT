from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    matricula = models.CharField(max_length=14, null=True, verbose_name="MATRÍCULA")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)