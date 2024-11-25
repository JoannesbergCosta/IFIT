from django import forms
from .models import Task
from django.forms import DateInput


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "programa_treino",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Insira o título do evento"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira a descrição do evento",
                }
            ),
            "start_date": DateInput(attrs={"class": "form-control", "type": "date"}),
            "end_date": DateInput(attrs={"class": "form-control", "type": "date"}),
            "start_time": DateInput(attrs={"class": "form-control", "type": "time"}),
            "end_time": DateInput(attrs={"class": "form-control", "type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        from cadastros.models import TrainingExercicio  # Importação dinâmica
        super().__init__(*args, **kwargs)
        self.fields["programa_treino"] = forms.ModelChoiceField(
            queryset=TrainingExercicio.objects.all(),
            required=True,
            label="Programa de Treinamento",
            widget=forms.Select(
                attrs={
                    "class": "form-select",
                    "aria-label": "Selecionar programa de treino",
                }
            ),
        )
