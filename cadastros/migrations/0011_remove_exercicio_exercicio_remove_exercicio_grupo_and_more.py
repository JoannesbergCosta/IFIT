# Generated by Django 5.1.1 on 2024-11-28 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0010_delete_userauth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercicio',
            name='exercicio',
        ),
        migrations.RemoveField(
            model_name='exercicio',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='exercicio',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='trainingexercicio',
            name='carga',
        ),
        migrations.RemoveField(
            model_name='trainingexercicio',
            name='descanso',
        ),
        migrations.RemoveField(
            model_name='trainingexercicio',
            name='exercises',
        ),
        migrations.RemoveField(
            model_name='trainingexercicio',
            name='repeticoes',
        ),
        migrations.RemoveField(
            model_name='trainingexercicio',
            name='series',
        ),
        migrations.RemoveField(
            model_name='trainingexercicio',
            name='usuario',
        ),
        migrations.AddField(
            model_name='exercicio',
            name='nome',
            field=models.CharField(default='Default Name', max_length=100),
        ),
        migrations.AddField(
            model_name='exercicio',
            name='programa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exercicios', to='cadastros.trainingexercicio'),
        ),
        migrations.AddField(
            model_name='trainingexercicio',
            name='nome',
            field=models.CharField(default='Default Name', max_length=100),
        ),
        migrations.AddField(
            model_name='trainingexercicio',
            name='tipo_treino',
            field=models.CharField(default='Desconhecido', max_length=100),
        ),
        migrations.AlterField(
            model_name='exercicio',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trainingexercicio',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField()),
                ('repeticoes', models.PositiveIntegerField()),
                ('carga', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('tempo', models.DurationField()),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='cadastros.exercicio')),
            ],
        ),
    ]