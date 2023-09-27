from rest_framework import serializers
from .models import *


class  ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Professor
        fields =['id','nome','email','senha']

class  TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Turma
        fields =['id','nome_turma','observacao']


class  Professor_turmaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Professor_turma
        fields =['id','fk_turma','fk_professor','materia']


class  AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Atividade
        fields =['id','nome','peso','descricao','fk_professor']


class  Turma_atividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Turma_atividade
        fields =['id','dt_inicio','dt_fim','fk_atividade','fk_turma']