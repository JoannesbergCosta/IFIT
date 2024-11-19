# Generated by Django 5.1.1 on 2024-11-18 22:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_userauth_user_alter_trainingexercicio_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('idade', models.PositiveIntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pescoco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ombro_dir', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ombro_esq', models.DecimalField(decimal_places=2, max_digits=5)),
                ('braco_relaxado_dir', models.DecimalField(decimal_places=2, max_digits=5)),
                ('braco_relaxado_esq', models.DecimalField(decimal_places=2, max_digits=5)),
                ('braco_contraido_dir', models.DecimalField(decimal_places=2, max_digits=5)),
                ('braco_contraido_esq', models.DecimalField(decimal_places=2, max_digits=5)),
                ('antebraco_dir', models.DecimalField(decimal_places=2, max_digits=5)),
                ('antebraco_esq', models.DecimalField(decimal_places=2, max_digits=5)),
                ('torax_relaxado', models.DecimalField(decimal_places=2, max_digits=5)),
                ('torax_contraido', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cintura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quadril', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coxa_dir', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coxa_esq', models.DecimalField(decimal_places=2, max_digits=5)),
                ('panturrilha_dir', models.DecimalField(decimal_places=2, max_digits=5)),
                ('panturrilha_esq', models.DecimalField(decimal_places=2, max_digits=5)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]