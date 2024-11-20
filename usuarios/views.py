from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def custom_logout_view(request):
    logout(request)
    return redirect('login')  


class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo, _ = Group.objects.get_or_create(name="Docente")

        url = super().form_valid(form)

        self.object.groups.add(grupo)

        Perfil.objects.get_or_create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context


class PerfilUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Perfil
    fields = ['nome_completo', 'email', 'matricula']
    success_url = reverse_lazy("inicio")

    def get_object(self, queryset=None):
        # Obtém ou cria o perfil do usuário
        perfil, _ = Perfil.objects.get_or_create(usuario=self.request.user)
        return perfil

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Meus dados"
        context['botao'] = "Atualizar"
        return context


 