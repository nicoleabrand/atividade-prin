from django.contrib import admin
from .models import Livro, Aluno, Emprestimo
# Register your models here.

admin.site.register(Aluno)
admin.site.register(Livro)
admin.site.register(Emprestimo)