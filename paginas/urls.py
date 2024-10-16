# myproject/paginas/urls.py

from django.urls import path
from .views import IndexView, SobreView, CustomLoginView, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),   
    path('login/', CustomLoginView.as_view(), name='login'),
    #path('logout/', logoutview, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),  
    
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), #alterar senha
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #email enviado
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
