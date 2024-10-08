
from django.urls import path

from .views import CampoCreate, UserCreate
from .views import CampoUpdate, UserUpdate
from .views import CampoDelete, UserDelete
from .views import CampoList, UserList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/user/', UserCreate.as_view(), name="cadastrar-user"),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name="editar-campo"),
    path('editar/user/<int:pk>/', UserUpdate.as_view(), name="editar-user"),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name="excluir-campo"),
    path('excluir/user/<int:pk>/', UserDelete.as_view(), name="excluir-user"),

    path('listar/campos/', CampoList.as_view(), name="listar-campos"),
    path('listar/users/', UserList.as_view(), name="listar-users"),
   
]
