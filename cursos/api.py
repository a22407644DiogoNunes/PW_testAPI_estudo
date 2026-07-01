from ninja import NinjaAPI
from .models import Professor, Aluno, Curso
from typing import List
from .schemas import *
from django.shortcuts import get_object_or_404

api = NinjaAPI(
    title="Api dos Cursos",
    description="Api com os alunos e professores associados aos cursos",
    version="1.0.0"
)

#----------------Listar---------------------#

@api.get(
        'aluno/',
        response=List[AlunoOut],
        tags=["Aluno"],
        description="Lista todos os alunos"
)
def lista_aluno(request):
    aluno = Aluno.objects.all()
    return aluno

@api.get('professor/', response=List[ProfessorOut], tags=["Professor"], description="Lista todos os professores")
def lista_professor(request, sort: str = None, nome: str = None):
    professor = Professor.objects.all()
    
    if sort in ('nome', 'email', '-nome', '-email'):
        professor=professor.objects.order_by(sort)
    
    if nome:
        professor = professor.filter(nome__contains=nome)

    return professor

@api.get('curso/', response=List[CursoOut], tags=["Curso"], description="Lista todos os cursos")
def lista_curso(request):
    return Curso.objects.all()

#------------------Criar-------------------#

@api.post(
        "aluno/",
        response={
            200:AlunoOut,
            400:ErrorSchema
        },
        tags=["Aluno"],
        description="Cria Aluno"
)
def criar_aluno(request, data:AlunoIn):

    if Aluno.objects.filter(numero=data.numero).exists():
        return 400, {"mensagem":"numero de aluno já existente"}

    aluno = Aluno.objects.create(**data.dict())
    return 200, aluno

@api.post(
    'professor/',
    response={
        200: ProfessorOut,
        400: ErrorSchema
    },
    tags=["Professor"]
)
def criar_professor(request, data:ProfessorIn):
    if Professor.objects.filter(email=data.email).exists():
        return 400, {'mensagem':"email já existente"}
    
    professor = Professor.objects.create(**data.dict())
    return 200, professor

@api.post(
    'curso/',
    response={
        200: CursoOut,
        400: ErrorSchema
    },
    tags=["Curso"]
)
def criar_curso(request, data:CursoIn):
    professor = get_object_or_404(Professor, id=data.professor_id)

    curso = Curso.objects.create(
        nome=data.nome,
        professor=professor
    )

    curso.alunos.set(data.alunos_ids)
    return 200, curso

#---------------Substituir--------------#

@api.put(
        "aluno/{id}",
        response={
            200: AlunoOut,
            400: ErrorSchema,
            404: ErrorSchema,
        },
        tags=["Aluno"],
        description="Atualizar dados do aluno"
)
def substituir_dados_aluno(request, id:int, data:AlunoIn):
    aluno = get_object_or_404(Aluno, id=id)

    for atributo, valor in data.dict().items():
        setattr(aluno, atributo, valor)

    aluno.save()

    return 200, aluno

@api.put(
    'professor/{id}',
    response={
        200: ProfessorOut,
        400: ErrorSchema,
        404: ErrorSchema
    },
    tags=["Professor"]
)
def substituir_dados_professor(request, id:int, data:ProfessorIn):
    professor = get_object_or_404(Professor, id=id)
    # professor.nome = data.nome
    # professor.email = data.email

    for atributo, valor in data.dict().items():
        setattr(professor, atributo, valor)

    professor.save()

    return 200, professor

@api.put(
    "cursos/{id}",
    response={
        200:CursoOut,
        400:ErrorSchema,
        404:ErrorSchema
    },
    tags=["Curso"]
)
def substituir_dados_curso(request, id:int, data:CursoIn):
    curso = get_object_or_404(Curso, id=id)
    professor  = get_object_or_404(Professor,id = data.professor_id)

    curso.nome = data.nome
    curso.professor = professor

    curso.save()

    curso.alunos.set(data.alunos_ids)

    return 200,curso

#-------------------Buscar---------------------#

@api.get(
        "aluno/{id}",
        response={
            200:AlunoOut,
            404:ErrorSchema,
        },
        tags=["Aluno"]
)
def buscar_aluno(request, aluno_id:int):
    aluno = get_object_or_404(Aluno, id = aluno_id)
    return 200, aluno

@api.get(
    "professor/{id}",
    response={
        200:ProfessorOut,
        404:ErrorSchema
    },
    tags=["Professor"]
)
def buscar_professor(request,id:int):
    professor = get_object_or_404(Professor,id=id)
    
    return 200,professor

@api.get(
    "curso/{id}",
    response={
        200:CursoOut,
        404:ErrorSchema
    },
    tags=["Curso"]
)
def buscar_curso(request,id:int):
    curso = get_object_or_404(Curso, id=id)

    return 200,curso

#----------------------Delete-------------#

@api.delete(
        "aluno/{id}",
        response={
            204: None,
            404: ErrorSchema
        },
        tags=["Aluno"],
        description="Apagar aluno da base de dados"
)
def apaga_aluno(request, id:int):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()

    return 204, None

@api.delete(
    "professor/{id}",
    response={
        204:None,
        404:ErrorSchema,
    },
    tags=["Professor"]
)
def apaga_professor(request, id:int):
    professor = get_object_or_404(Professor, id=id)
    professor.delete()

    return 204,None

@api.delete(
    "curso/{id}",
    response={
        204:None,
        404:ErrorSchema
    },
    tags=["Curso"]
)
def apaga_curso(request, id:int):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()

    return 204,None