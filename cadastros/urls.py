
from django.urls import path

from .views import CampoCreate, UserAuthCreate, ExercicioCreate, TrainingExercicioCreate
from .views import CampoUpdate, UserAuthUpdate, ExercicioUpdate, TrainingExercicioUpdate
from .views import CampoDelete, UserAuthDelete, ExercicioDelete, TrainingExercicioDelete
from .views import CampoList, UserAuthList, ExercicioList, TrainingExercicioList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/userauth/', UserAuthCreate.as_view(), name='cadastrar-userauth'),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/userauth/<int:pk>/', UserAuthUpdate.as_view(), name='editar-userauth'),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/userauth/<int:pk>/', UserAuthDelete.as_view(), name='excluir-userauth'),

    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/usersauth/', UserAuthList.as_view(), name='listar-usersauth'),
   
     # URLs para Exercicio
    path('cadastrar/exercicio/', ExercicioCreate.as_view(), name='cadastrar-exercicio'),
    path('editar/exercicio/<int:pk>/', ExercicioUpdate.as_view(), name='editar-exercicio'),
    path('excluir/exercicio/<int:pk>/', ExercicioDelete.as_view(), name='excluir-exercicio'),
    path('listar/exercicios/', ExercicioList.as_view(), name='listar-exercicios'),

    # URLs para TrainingExercicio
    path('cadastrar/training-exercicio/', TrainingExercicioCreate.as_view(), name='cadastrar-training-exercicio'),
    path('editar/training-exercicio/<int:pk>/', TrainingExercicioUpdate.as_view(), name='editar-training-exercicio'),
    path('excluir/training-exercicio/<int:pk>/', TrainingExercicioDelete.as_view(), name='excluir-training-exercicio'),
    path('listar/training-exercicios/', TrainingExercicioList.as_view(), name='listar-training-exercicios'),

]
