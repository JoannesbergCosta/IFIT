from django.views.generic.edit import CreateView, DeleteView
from .models import Campo, User
from django.urls import reverse_lazy

# Create your views here.
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