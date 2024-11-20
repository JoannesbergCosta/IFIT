from django import forms
from .models import TrainingExercicio, Exercicio

class TrainingExercicioForm(forms.ModelForm):
    class Meta:
        model = TrainingExercicio
        fields = ['usuario','exercises', 'series', 'repeticoes', 'carga', 'descanso', 'descricao']

    # Permitir selecionar múltiplos exercícios
    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercicio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            exercises = self.instance.exercises.all()
            for i, exercise in enumerate(exercises):
                self.fields[f'series_{i}'] = forms.IntegerField(label=f'Série do exercício {exercise.exercicio}')
                self.fields[f'repeticoes_{i}'] = forms.IntegerField(label=f'Repetições do exercício {exercise.exercicio}')
                self.fields[f'carga_{i}'] = forms.CharField(label=f'Carga do exercício {exercise.exercicio}', required=False)
                self.fields[f'descanso_{i}'] = forms.IntegerField(label=f'Descanso do exercício {exercise.exercicio}')
