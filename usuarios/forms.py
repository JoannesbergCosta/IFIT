from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data.get('email')
        if User.objects.filter(email=e).exists():
            raise ValidationError(f"O email {e} já está em uso.")
        return e




