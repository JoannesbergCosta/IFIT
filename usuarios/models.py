from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    matricula = models.CharField(max_length=14, null=True, verbose_name="MATRICULA")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


class IMCRegistro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    peso = models.FloatField()
    altura = models.FloatField()
    imc = models.FloatField(editable=False)
    data_registro = models.DateTimeField(default=timezone.now)

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def save(self, *args, **kwargs):
        self.imc = self.calcular_imc()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.data_registro.strftime("%d/%m/%Y")}'