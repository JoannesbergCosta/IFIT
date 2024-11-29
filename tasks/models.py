from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from cadastros.models import TrainingExercicio

class Task(models.Model):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_subs = models.PositiveIntegerField(default=0)
    subs = models.PositiveIntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError('A data de início não pode ser posterior à data de fim.')
        elif self.start_date is None or self.end_date is None:
            raise ValidationError('Ambas as datas de início e fim devem ser fornecidas.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)