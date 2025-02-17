from rest_framework.serializers import ModelSerializer
from .models import Alunos, Livros, Emprestimos

class AlunosSerializer(ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'

class LivrosSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'

class EmprestimosSerializer(ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = '__all__'