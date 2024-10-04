from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"[Campo: {self.nome}]"
    

class User(models.Model):
    matricula = models.IntegerField(
        verbose_name="Matrícula",
        validators=[MinValueValidator(10000000000000), MaxValueValidator(99999999999999)]
    )
    #email =
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"[User: {self.nome}] (Campo: {self.campo.nome})"
