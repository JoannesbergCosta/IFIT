from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campo, User, Exercicio, TrainingExercicio
from django.urls import reverse_lazy

# Create Views
class CampoCreate(CreateView):
    model = Campo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class UserCreate(CreateView):
    model = User
    fields = ['matricula', 'campo', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-users')

class ExercicioCreate(CreateView):
    model = Exercicio
    fields = ['exercicio', 'tipo', 'grupo', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-exercicios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercicios'] = Exercicio.objects.all()  # Passa a lista de exercícios para o template
        return context

class TrainingExercicioCreate(CreateView):
    model = TrainingExercicio
    fields = ['pt', 'exercise', 'exercise', 'series', 'repeticoes', 'carga', 'descanso']  # Removido 'training'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-training-exercicios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercicios'] = Exercicio.objects.all()  # Passa a lista de exercícios para o template
        return context

# Update Views
class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class UserUpdate(UpdateView):
    model = User
    fields = ['matricula', 'campo', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-users')

class ExercicioUpdate(UpdateView):
    model = Exercicio
    fields = ['exercicio', 'tipo', 'grupo', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-exercicios')

class TrainingExercicioUpdate(UpdateView):
    model = TrainingExercicio
    fields = ['pt', 'exercise', 'exercise', 'series', 'repeticoes', 'carga', 'descanso']  # Removido 'training'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-training-exercicios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercicios'] = Exercicio.objects.all()  # Passa a lista de exercícios para o template
        return context

# Delete Views
class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class UserDelete(DeleteView):
    model = User
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-users')

class ExercicioDelete(DeleteView):
    model = Exercicio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-exercicios')

class TrainingExercicioDelete(DeleteView):
    model = TrainingExercicio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-training-exercicios')

# List Views
class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'

class UserList(ListView):
    model = User
    template_name = 'cadastros/listas/user.html'

class ExercicioList(ListView):
    model = Exercicio
    template_name = 'cadastros/listas/exercicio.html'

class TrainingExercicioList(ListView):
    model = TrainingExercicio
    template_name = 'cadastros/listas/training_exercicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['training_exercicio'] = TrainingExercicio.objects.select_related('exercise').all()  # Removido 'training'
        return context
