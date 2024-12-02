from django.db import models
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User



def get_default_exercicio():
    return Exercicio.objects.first()

class Campo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"[Campo: {self.nome}]"

class Exercicio(models.Model):
    nome = models.CharField(max_length=100, default='Default Name')
    tipo = models.CharField(max_length=50, choices=[('Força', 'Força'), ('Cardio', 'Cardio'), ('Flexibilidade', 'Flexibilidade')], default='Força')

    def __str__(self):
        return self.nome

class TrainingExercicio(models.Model):
    exercicio = models.ForeignKey(Exercicio, related_name='treinamentos', on_delete=models.CASCADE, default=get_default_exercicio)
    nome_programa = models.CharField(max_length=100)
    grupo = models.CharField(max_length=50, default='Desconhecido') 
    series = models.PositiveIntegerField(default=10)
    repeticoes = models.PositiveIntegerField(default=10)
    carga = models.IntegerField(default=0, verbose_name="Carga (kg)")
    tempo = models.IntegerField(default=0, verbose_name="Minutos (mn)")  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return f'{self.nome_programa} - {self.grupo}'
    

class Avaliacao(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()  
    idade = models.PositiveIntegerField()  
    peso = models.DecimalField(max_digits=5, decimal_places=2)  
    altura = models.DecimalField(max_digits=4, decimal_places=2)  
    pescoco = models.DecimalField(max_digits=5, decimal_places=2)  
    ombro_dir = models.DecimalField(max_digits=5, decimal_places=2)
    ombro_esq = models.DecimalField(max_digits=5, decimal_places=2)
    braco_relaxado_dir = models.DecimalField(max_digits=5, decimal_places=2)
    braco_relaxado_esq = models.DecimalField(max_digits=5, decimal_places=2)
    braco_contraido_dir = models.DecimalField(max_digits=5, decimal_places=2)
    braco_contraido_esq = models.DecimalField(max_digits=5, decimal_places=2)
    antebraco_dir = models.DecimalField(max_digits=5, decimal_places=2)
    antebraco_esq = models.DecimalField(max_digits=5, decimal_places=2)
    torax_relaxado = models.DecimalField(max_digits=5, decimal_places=2)
    torax_contraido = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    quadril = models.DecimalField(max_digits=5, decimal_places=2)
    coxa_dir = models.DecimalField(max_digits=5, decimal_places=2)
    coxa_esq = models.DecimalField(max_digits=5, decimal_places=2)
    panturrilha_dir = models.DecimalField(max_digits=5, decimal_places=2)
    panturrilha_esq = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Avaliação de {self.usuario.first_name} {self.usuario.last_name} | Data: {self.data} | Hora: {self.hora}"
