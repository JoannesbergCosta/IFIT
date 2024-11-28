from django.contrib import admin
from .models import Campo, Exercicio, TrainingExercicio, Avaliacao

admin.site.register(Campo)
admin.site.register(Exercicio)
admin.site.register(TrainingExercicio)
admin.site.register(Avaliacao)