from django import forms
from django.contrib.auth.forms import AuthenticationForm
from cadastros.models import TrainingExercicio  # Importar do app correto

class TrainingExercicioForm(forms.ModelForm):
    class Meta:
        model = TrainingExercicio
        fields = ['descricao', 'exercises', 'series', 'repeticoes', 'carga', 'descanso']
        widgets = {
            'exercises': forms.CheckboxSelectMultiple,
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu usuário',
        })
    )
    
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        })
    )
