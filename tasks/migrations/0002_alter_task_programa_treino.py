# Generated by Django 5.1.1 on 2024-11-28 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0010_delete_userauth'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='programa_treino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.trainingexercicio'),
        ),
    ]
