from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .models import IMCRegistro
from .forms import IMCForm

from django.contrib.auth.decorators import login_required


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
        # Se o usuário é staff, ele pode ver todos os perfis
        if self.request.user.is_staff:
            queryset = Perfil.objects.all()
        else:
            # Usuário comum só pode ver o próprio perfil
            queryset = Perfil.objects.filter(usuario=self.request.user)
        
        # Aplicar o filtro de nome_completo, se existir
        txt_nome = self.request.GET.get('nome_completo')
        if txt_nome:
            queryset = queryset.filter(nome_completo__icontains=txt_nome)  # Ajuste aqui
        
        return queryset

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


@login_required
def calcular_imc(request):
    if request.method == 'POST':
        form = IMCForm(request.POST)
        if form.is_valid():
            imc_registro = form.save(commit=False)
            imc_registro.user = request.user
            imc_registro.save()
            return redirect('progresso_imc')
    else:
        form = IMCForm()
    return render(request, 'calcular_imc.html', {'form': form})

@login_required
def progresso_imc(request):
    registros = IMCRegistro.objects.filter(user=request.user).order_by('-data_registro')
    return render(request, 'progresso_imc.html', {'registros': registros})

def apagar_imc(request, imc_id):
    
    imc_registro = get_object_or_404(IMCRegistro, id=imc_id, user=request.user) 
    
    imc_registro.delete()
    
    return redirect('progresso_imc')