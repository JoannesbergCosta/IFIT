from django import forms
from .models import TrainingExercicio

class TrainingExercicioForm(forms.ModelForm):
    class Meta:
        model = TrainingExercicio
        fields = ['exercises', 'series', 'repeticoes', 'carga', 'descanso', 'descricao']
