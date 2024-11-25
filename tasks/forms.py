from django import forms
from .models import Task
from django.forms import DateInput
from django import forms
from classes import models

class TaskForm(forms.ModelForm):
    turma = forms.ModelChoiceField(queryset=models.Turma.objects.all(), required=True)
    class Meta:
        model = Task
        fields = ["title", "description", "turma", "start_date", "end_date", "start_time", "end_time"]

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
            "turma": forms.Select(
                attrs={
                    "class": "form-select",  # Adicionando a classe do Bootstrap
                    "aria-label": "Selecionar turma"  # Para acessibilidade
                }
            ),
            "start_date": DateInput(
                attrs={"class": "form-control"},
            ),
            "end_date": DateInput(
                attrs={"class": "form-control"},
            ),
            "start_time": DateInput(
                attrs={"class": "form-control"},
            ),
            "end_time": DateInput(
                attrs={"class": "form-control"},
            ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        task = super().save(commit=False)
        task.id_turma = self.cleaned_data['turma'].id  # Armazena o ID da turma selecionada
        if commit:
            task.save()
        return task