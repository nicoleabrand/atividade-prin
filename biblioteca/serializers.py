from rest_framework.serializers import ModelSerializer
from .models import Aluno, Livro, Emprestimo

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'