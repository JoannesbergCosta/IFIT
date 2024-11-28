from django.db.models.query import QuerySet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campo, Exercicio, TrainingExercicio, Avaliacao
from django.urls import reverse_lazy
from .forms import TrainingExercicioForm, ExercicioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect

# Create Views
class CampoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome']
    form_class = ExercicioForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class ExercicioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')  # Redireciona para a página de login se não autenticado
    group_required = u"Administrador"  # Restringe o acesso ao grupo "Administrador"
    model = Exercicio  # Modelo para o qual o formulário será gerado
    template_name = 'cadastros/form.html'  # Caminho para o template do formulário
    success_url = reverse_lazy('listar-exercicios')  # URL para redirecionamento após sucesso

    # Especificando os campos que aparecerão no formulário
    fields = ['nome', 'tipo', 'grupo', 'series', 'repeticoes', 'carga', 'tempo']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastrar Exercício"  # Título para exibir no template
        context['botao'] = "Salvar"  # Texto do botão de submissão
        return context
    
class AvaliacaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Avaliacao
    fields = ['usuario', 'data', 'hora', 'idade', 'peso', 'altura', 'pescoco', 
              'ombro_dir', 'ombro_esq', 'braco_relaxado_dir', 'braco_relaxado_esq', 
              'braco_contraido_dir', 'braco_contraido_esq', 'antebraco_dir', 
              'antebraco_esq', 'torax_relaxado', 'torax_contraido', 'cintura', 
              'quadril', 'coxa_dir', 'coxa_esq', 'panturrilha_dir', 'panturrilha_esq']
    template_name = 'cadastros/form_avaliacao.html'
    success_url = reverse_lazy('listar-avaliacoes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Avaliação Fisica"
        context['botao'] = "Cadastrar Avaliação"

        return context


class TrainingExercicioCreate(CreateView):
    model = TrainingExercicio
    form_class = TrainingExercicioForm
    template_name = 'cadastros/form.html'
    success_url = '/listar/training-exercicios/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Treinamento'
        context['botao'] = 'Salvar'
        return context



# Update Views
class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class ExercicioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Exercicio
    fields = ['exercicio', 'tipo', 'grupo', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-exercicios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Exercício"
        context['botao'] = "Salvar"

        return context

class AvaliacaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Avaliacao
    fields = ['usuario', 'data', 'hora', 'idade', 'peso', 'altura', 'pescoco', 
              'ombro_dir', 'ombro_esq', 'braco_relaxado_dir', 'braco_relaxado_esq', 
              'braco_contraido_dir', 'braco_contraido_esq', 'antebraco_dir', 
              'antebraco_esq', 'torax_relaxado', 'torax_contraido', 'cintura', 
              'quadril', 'coxa_dir', 'coxa_esq', 'panturrilha_dir', 'panturrilha_esq']
    template_name = 'cadastros/form_avaliacao.html'
    success_url = reverse_lazy('listar-avaliacoes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Avaliação"
        context['botao'] = "Salvar"

        return context


class TrainingExercicioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = TrainingExercicio
    form_class = TrainingExercicioForm
    template_name = 'cadastros/form_training_exercicio.html'
    success_url = reverse_lazy('listar-training-exercicios')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Você não tem permissão para editar este registro.")
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(TrainingExercicio, pk=self.kwargs['pk'])



# Delete Views
class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class ExercicioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Exercicio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-exercicios')

class AvaliacaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Avaliacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-avaliacoes')

class TrainingExercicioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = TrainingExercicio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-training-exercicios')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('listar-training-exercicios')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(TrainingExercicio, pk=self.kwargs['pk'])

    
# List Views
class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

class ExercicioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Exercicio
    template_name = 'cadastros/listas/exercicio.html'

class TrainingExercicioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = TrainingExercicio
    template_name = 'cadastros/listas/training_exercicio.html'
    paginate_by = 3
    context_object_name = 'programas'

    def get_queryset(self):
        if self.request.user.is_staff:
            return TrainingExercicio.objects.all() 
        else:
            return TrainingExercicio.objects.filter(usuario=self.request.user) 


class AvaliacaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    template_name = 'cadastros/listas/avaliacao.html'
    paginate_by = 1

    def get_queryset(self):
        if self.request.user.is_staff:
            return Avaliacao.objects.all()  
        else:
            return Avaliacao.objects.filter(usuario=self.request.user)  



