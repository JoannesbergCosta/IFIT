from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def custom_logout_view(request):
    # Realiza o logout do usuário e redireciona para a página de login
    logout(request)
    return redirect('login')


class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Criar o grupo 'Docente' caso não exista
        grupo, _ = Group.objects.get_or_create(name="Docente")

        # Salvar o formulário do usuário
        url = super().form_valid(form)

        # Adicionar o usuário ao grupo 'Docente'
        self.object.groups.add(grupo)

        # Criar o perfil do usuário
        Perfil.objects.get_or_create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context


class PerfilList(ListView):
    login_url = reverse_lazy('login')  # Redireciona para login caso o usuário não esteja autenticado
    model = Perfil
    template_name = 'cadastros/listas/userauth.html'

    def get_queryset(self):
        # Verifica se o usuário é staff ou não
        if self.request.user.is_staff:
            return Perfil.objects.all()  # Se for staff, retorna todos os perfis
        else:
            return Perfil.objects.filter(usuario=self.request.user)  # Caso contrário, apenas o perfil do usuário logado

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Lista de Usuários"
        return context


class PerfilUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Perfil
    fields = ['nome_completo', 'email', 'matricula']
    success_url = reverse_lazy("inicio")

    def get_object(self, queryset=None):
        # Obtém o perfil do usuário logado, criando-o caso não exista
        perfil, _ = Perfil.objects.get_or_create(usuario=self.request.user)
        return perfil

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Meus dados"
        context['botao'] = "Atualizar"
        return context
