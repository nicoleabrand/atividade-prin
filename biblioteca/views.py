from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Livro, Emprestimo, Aluno
from .serializers import LivroSerializer, EmprestimoSerializer, AlunoSerializer

class LivrosViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class EmprestimosViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class AlunosViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
# Create your views here.
