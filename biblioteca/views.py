from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Livros, Emprestimos, Alunos
from .serializers import LivrosSerializer, EmprestimosSerializer, AlunosSerializer

class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class EmprestimosViewSet(ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer

class AlunosViewSet(ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer
# Create your views here.
