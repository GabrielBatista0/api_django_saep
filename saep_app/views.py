from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from .serializer import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset =  Professor.objects.all()
    serializer_class =  ProfessorSerializer

    def create(self, request, *args, **kwargs):
        dados = request.data
        new_professor = Professor.objects.create(
            nome = dados['nome'],
            email = dados['email'],
            senha = make_password(dados['senha'])
        )
        serializer = ProfessorSerializer(new_professor)
        return Response(serializer.data)
    

class LoginProfessorViewSet(viewsets.ModelViewSet):
    queryset =  Professor.objects.all()
    serializer_class =  ProfessorSerializer
    def create(self, request, *args, **kwargs):
        dados = request.data
        usuario = get_object_or_404(Professor, email = dados['email'])
        if(check_password(dados['senha'],usuario.senha)):
            return Response({"Response":f"Usuario {usuario.nome} autorizado"},200)
        else:
            return Response({"Response":f"Usuario não autorizado"},401)



class TurmaViewSet(viewsets.ModelViewSet):
    queryset =  Turma.objects.all()
    serializer_class =  TurmaSerializer

class Professor_turmaViewSet(viewsets.ModelViewSet):
    queryset =  Professor_turma.objects.all()
    serializer_class =  Professor_turmaSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset =  Atividade.objects.all()
    serializer_class =  AtividadeSerializer

class Turma_atividadeViewSet(viewsets.ModelViewSet):
    queryset =  Turma_atividade.objects.all()
    serializer_class =  Turma_atividadeSerializer

    