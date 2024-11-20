
from django.urls import path

from .views import (
    CampoCreate, ExercicioCreate, TrainingExercicioCreate, AvaliacaoCreate,
    CampoUpdate, ExercicioUpdate, TrainingExercicioUpdate, AvaliacaoUpdate,
    CampoDelete, ExercicioDelete, TrainingExercicioDelete, AvaliacaoDelete,
    CampoList, ExercicioList, TrainingExercicioList, AvaliacaoList
)

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('listar/campos/', CampoList.as_view(), name='listar-campos'),

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

    # URLs para Avaliação
    path('cadastrar/avaliacao/', AvaliacaoCreate.as_view(), name='cadastrar-avaliacao'),
    path('editar/avaliacao/<int:pk>/', AvaliacaoUpdate.as_view(), name='editar-avaliacao'),
    path('excluir/avaliacao/<int:pk>/', AvaliacaoDelete.as_view(), name='excluir-avaliacao'),
    path('listar/avaliacoes/', AvaliacaoList.as_view(), name='listar-avaliacoes'),
]

