# Generated by Django 4.1.2 on 2022-10-28 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('materia', models.CharField(max_length=30)),
            ],
        ),
    ]
