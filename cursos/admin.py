from django.contrib import admin
from .models import Professor,Aluno,Curso

# Register your models here.
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome","email",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Professor,ProfessorAdmin)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero",)
    ordering = ("numero",)
    search_fields = ("numero",)

admin.site.register(Aluno,AlunoAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)
    filter_horizontal = ("alunos",)

admin.site.register(Curso,CursoAdmin)