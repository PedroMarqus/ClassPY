from app.database.connection import get_connection

def criar_aluno(nome, idade):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO alunos (nome, idade) VALUES (?, ?)",
        (nome, idade)
    )

    conn.commit()
    conn.close()


def listar_alunos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    conn.close()
    return alunos

def buscar_aluno_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos WHERE nome LIKE ?", ('%' + nome + '%',))
    alunos = cursor.fetchall()

    conn.close()
    return alunos