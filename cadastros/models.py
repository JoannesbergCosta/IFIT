from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Campo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"[Campo: {self.nome}]"


class Exercicio(models.Model):
    exercicio = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10)
    grupo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.exercicio
    
class TrainingExercicio(models.Model):
    exercises = models.ManyToManyField(Exercicio)
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    carga = models.CharField(max_length=50, blank=True, null=True)
    descanso = models.IntegerField()  # em segundos
    descricao = models.CharField(max_length=100, default='Descrição padrão')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        exercicios = ', '.join([exercise.exercicio for exercise in self.exercises.all()])
        return f"Programa: {self.descricao} | Exercícios: {exercicios}"
    
    
class Avaliacao(models.Model):
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
        # Usando first_name e last_name do usuário para criar o nome completo
        return f"Avaliação de {self.usuario.first_name} {self.usuario.last_name} | Data: {self.data} | Hora: {self.hora}"


