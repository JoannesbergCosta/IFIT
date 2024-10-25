# myproject/paginas/views.py

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import LoginForm

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# View para a página inicial
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "paginas/index.html"

# View para a página "Sobre"
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

# View personalizada para login
class CustomLoginView(LoginView):
    template_name = 'login.html'  
    authentication_form = LoginForm  

# View para registro de novos usuários
class RegisterView(TemplateView):
    template_name = 'registration/register.html'  

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()  # Cria um novo formulário de registro
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            login(request, user)  # Faz login automático do usuário
            return redirect('inicio')  # Redireciona para a página inicial
        return render(request, self.template_name, {'form': form})  # Retorna ao template em caso de erro




