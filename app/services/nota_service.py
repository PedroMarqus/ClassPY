from app.repositories import nota_repository

def criar_nota(aluno_id, disciplina, nota):
    if aluno_id is None:
        raise ValueError("ID do aluno é obrigatório")
    if disciplina is None:
        raise ValueError("Disciplina é obrigatória")
    if nota is None:
        raise ValueError("Nota é obrigatória")
    nota_repository.criar_nota(aluno_id, disciplina, nota)

def listar_notas():
    return nota_repository.listar_notas()