from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Campo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"[Campo: {self.nome}]"

class UserAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Associa UserAuth com User
    matricula = models.IntegerField(
        verbose_name="Matrícula",
        validators=[MinValueValidator(10000000000000), MaxValueValidator(99999999999999)]
    )
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"Usuário: {self.nome} | Matrícula: {self.matricula} | Campo: {self.campo.nome}"

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
