from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após logout
# Create your views here.
