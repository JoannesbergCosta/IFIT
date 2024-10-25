from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campo, User, Exercicio, TrainingExercicio
from django.urls import reverse_lazy
from .forms import TrainingExercicioForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Create Views
class CampoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class UserCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = User
    fields = ['matricula', 'campo', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-users')

class ExercicioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Exercicio
    fields = ['exercicio', 'tipo', 'grupo', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-exercicios')

class TrainingExercicioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = TrainingExercicio
    form_class = TrainingExercicioForm
    template_name = 'cadastros/form_training_exercicio.html'
    success_url = reverse_lazy('listar-training-exercicios')

# Update Views
class CampoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    fields = ['matricula', 'campo', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-users')

class ExercicioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Exercicio
    fields = ['exercicio', 'tipo', 'grupo', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-exercicios')

class TrainingExercicioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = TrainingExercicio
    form_class = TrainingExercicioForm
    template_name = 'cadastros/form_training_exercicio.html'
    success_url = reverse_lazy('listar-training-exercicios')

# Delete Views
class CampoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class UserDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-users')

class ExercicioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Exercicio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-exercicios')

class TrainingExercicioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = TrainingExercicio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-training-exercicios')

# List Views
class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

class UserList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'cadastros/listas/user.html'

class ExercicioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Exercicio
    template_name = 'cadastros/listas/exercicio.html'

class TrainingExercicioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = TrainingExercicio
    template_name = 'cadastros/listas/training_exercicio.html'
