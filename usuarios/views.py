from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil
from django.shortcuts import render, redirect
from django.contrib.auth import logout


class UsuarioCreate(CreateView):
    template_name = "cadastros/form_add_user.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        
        grupo, _ = Group.objects.get_or_create(name="Docente") #ou Discentes

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        
        Perfil.objects.get_or_create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context


class PerfilList(ListView):
    login_url = reverse_lazy('login')  
    model = Perfil
    template_name = 'cadastros/listas/userauth.html'
    paginate_by = 3

    def get_queryset(self):
        if self.request.user.is_staff:
            return Perfil.objects.all()  
        else:
            return Perfil.objects.filter(usuario=self.request.user)  

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Lista de Usuários"
        return context


class PerfilUpdate(UpdateView):
    template_name = "cadastros/form_perfil.html"
    model = Perfil
    fields = ['nome_completo', 'email', 'matricula']
    success_url = reverse_lazy("inicio")

    def get_object(self, queryset=None):
        perfil, _ = Perfil.objects.get_or_create(usuario=self.request.user)
        return perfil

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Meus dados"
        context['botao'] = "Atualizar"
        return context
    

def custom_logout_view(request):
    logout(request)
    return redirect('login')