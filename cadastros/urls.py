
from django.urls import path

from .views import CampoCreate, UserCreate

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/user/', UserCreate.as_view(), name="cadastrar-User"),
   
]
