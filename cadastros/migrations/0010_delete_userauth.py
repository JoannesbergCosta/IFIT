# Generated by Django 5.1.1 on 2024-11-20 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_avaliacao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAuth',
        ),
    ]