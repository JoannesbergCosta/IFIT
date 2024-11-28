from django import forms
from .models import TrainingExercicio, Exercicio

class TrainingExercicioForm(forms.ModelForm):
    class Meta:
        model = TrainingExercicio
        fields = ['exercicio', 'nome_programa', 'grupo', 'series', 'repeticoes', 'carga', 'tempo']

class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome' ,'tipo']