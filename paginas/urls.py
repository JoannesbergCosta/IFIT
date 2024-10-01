# myproject/paginas/urls.py

from django.urls import path
from .views import IndexView, SobreView, CustomLoginView, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),  # URL para a página inicial
    path('sobre/', SobreView.as_view(), name='sobre'),    # URL para a página "Sobre"
    path('login/', CustomLoginView.as_view(), name='login'),    # URL para a página de login
    path('register/', RegisterView.as_view(), name='register'),  # URL para a página de registro
    
    # URLs de redefinição de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
