from django.contrib import admin
from .models import Campo, User, Exercicio, TrainingExercicio
# Register your models here.
admin.site.register(Campo)
admin.site.register(User)
admin.site.register(Exercicio)
admin.site.register(TrainingExercicio)