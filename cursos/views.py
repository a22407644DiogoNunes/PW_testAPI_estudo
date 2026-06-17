from django.shortcuts import render
from .models import Curso,Aluno

def cursos_view(request):
    
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'cursos/cursos.html', {'cursos': cursos})

def curso_view(request, id):

    curso=Curso.objects.get(id=id)     

    return render(request, 'cursos/curso.html', {'curso': curso})

def alunos_view(request):
    alunos = Aluno.objects.all()
    return render(request, "cursos/alunos.html", {"alunos": alunos})