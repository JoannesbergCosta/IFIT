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

class Training(models.Model):
    descricao = models.CharField(max_length=50)
    objetivo = models.CharField(max_length=50)
    treinos = models.CharField(max_length=1) #treino A, B C...
    sessoes = models.IntegerField()

    class Meta:
        verbose_name_plural = "Trainings"

class TrainingExercicio(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='training_exercises')
    exercise = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    carga = models.CharField(max_length=50, blank=True, null=True)
    descanso = models.IntegerField()  # em segundos

    class Meta:
        verbose_name_plural = "Training Exercises"