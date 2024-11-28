from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class CustomLoginView(LoginView):
    template_name = 'login.html'  
    authentication_form = LoginForm  

class RegisterView(TemplateView):
    template_name = 'registration/register.html'  

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()  
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            login(request, user)  # Faz login automático do usuário
            return redirect('inicio')  # Redireciona para a página inicial
        return render(request, self.template_name, {'form': form})  # Retorna ao template em caso de erro




