# myproject/paginas/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuário',  # Rótulo para o campo de nome de usuário
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Adiciona a classe do Bootstrap
            'placeholder': 'Digite seu usuário',  # Placeholder para o campo
        })
    )
    
    password = forms.CharField(
        label='Senha',  # Rótulo para o campo de senha
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',  # Adiciona a classe do Bootstrap
            'placeholder': 'Digite sua senha',  # Placeholder para o campo
        })
    )
