from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from biblioteca.views import LivrosViewSet
from biblioteca.views import EmprestimosViewSet
from biblioteca.views import AlunosViewSet



router = DefaultRouter()
router.register(r'livros', LivrosViewSet)
router.register(r'emprestimos', EmprestimosViewSet)
router.register(r'alunos', AlunosViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]