from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano = models.IntegerField()
   
    def __str__(self):
        return self.titulo


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    dataemprestimo = models.DateField(blank=True, null=True)
    datadevolucao = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.livro} - ({self.aluno})'