# Generated by Django 4.2.5 on 2023-09-20 18:52

from django.db import migrations, models
import django.db.models.deletion
import saep_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.TextField(max_length=255)),
                ('nome_turma', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Turma_atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inicio', models.DateField()),
                ('dt_fim', models.DateField()),
                ('fk_atividade', models.DateField(verbose_name=saep_app.models.Atividade)),
                ('fk_turma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='saep_app.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Professor_turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=255)),
                ('fk_professor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='saep_app.professor')),
                ('fk_turma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='saep_app.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('peso', models.CharField(max_length=10)),
                ('descricao', models.TextField(max_length=255)),
                ('fk_professor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='saep_app.professor')),
            ],
        ),
    ]