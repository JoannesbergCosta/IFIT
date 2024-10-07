from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Campo, User
from django.urls import reverse_lazy

# views
############################## Create ##################################
class CampoCreate(CreateView):
    model = Campo
    fields = ['nome'] #COLOCAR OQUE QUER Q APAREÇA
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


class UserCreate(CreateView):
    model = User
    fields = ['matricula', 'campo', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


############################## Update ###################################
class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome'] #COLOCAR OQUE QUER Q APAREÇA
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


class UserUpdate(UpdateView):
    model = User
    fields = ['matricula','campo','nome'] #COLOCAR OQUE QUER Q APAREÇA
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


############################## Delete ###################################
class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')


class UserDelete(DeleteView):
    model = User
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')