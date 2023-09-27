from django.db import models



class Professor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.nome
    
class Turma(models.Model):
    observacao = models.TextField(max_length=255)
    nome_turma = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome_turma
    
class Professor_turma(models.Model):
    fk_professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    fk_turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    materia = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.materia
    
class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    peso = models.CharField(max_length=10)
    descricao = models.TextField(max_length=255)
    fk_professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
    
class Turma_atividade(models.Model):
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    fk_atividade = models.ForeignKey(Atividade, on_delete=models.DO_NOTHING)
    fk_turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)


    


