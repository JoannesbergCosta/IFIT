from django.contrib import admin
from .models import Campo, UserAuth, Exercicio, TrainingExercicio, Avaliacao
# Register your models here.
admin.site.register(Campo)
admin.site.register(UserAuth)
admin.site.register(Exercicio)
admin.site.register(TrainingExercicio)
admin.site.register(Avaliacao)