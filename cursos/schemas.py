from ninja import Schema
from typing import List

class ProfessorIn(Schema):
    nome: str
    email: str

class ProfessorOut(Schema):
    id: int
    nome: str
    email: str


class AlunoIn(Schema):
    nome: str
    numero: str

class AlunoOut(Schema):
    id: int
    nome: str
    numero: str

class CursoIn(Schema):
    nome:str
    professor_id: int
    alunos_ids: List[int] = []

class CursoOut(Schema):
    id: int
    professor: ProfessorOut
    alunos: List[AlunoOut] 

class ErrorSchema(Schema):
    mensagem: str