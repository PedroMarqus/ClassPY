from app.repositories import aluno_repository

def criar_aluno(nome, idade):
    if not nome:
        raise ValueError("Nome é obrigatório")

    aluno_repository.criar_aluno(nome, idade)


def listar_alunos():
    return aluno_repository.listar_alunos()

def buscar_aluno_por_nome(nome):
    if not nome:
        raise ValueError("Nome é obrigatório")

    return aluno_repository.buscar_aluno_por_nome(nome)