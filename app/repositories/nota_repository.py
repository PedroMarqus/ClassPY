from app.database.connection import get_connection

def criar_nota(aluno_id, disciplina, nota):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO notas (aluno_id, disciplina, nota) VALUES (?, ?, ?)",
        (aluno_id, disciplina, nota)
    )

    conn.commit()
    conn.close()

def listar_notas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            notas.id,
            alunos.id AS aluno_id,
            alunos.nome,
            notas.disciplina,
            notas.nota
        FROM notas
        JOIN alunos ON notas.aluno_id = alunos.id
    """)

    notas = cursor.fetchall()
    conn.close()
    return notas