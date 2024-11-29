from django import forms
from .models import Task
from django.forms import DateInput
from django.contrib.auth.models import User
from cadastros.models import TrainingExercicio

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'usuario', 
            "title",
            "description",
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
                attrs={ "class": "form-control", "placeholder": "Insira a descrição do evento" }
            ),
            "start_date": DateInput(attrs={"class": "form-control", "type": "date"}),
            "end_date": DateInput(attrs={"class": "form-control", "type": "date"}),
            "start_time": DateInput(attrs={"class": "form-control", "type": "time"}),
            "end_time": DateInput(attrs={"class": "form-control", "type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["usuario"] = forms.ModelChoiceField(
            queryset=User.objects.all(),
            required=True,
            label="Destinatário do Evento",
            widget=forms.Select(
                attrs={ "class": "form-select", "aria-label": "Selecionar usuário" }
            ),
        )
