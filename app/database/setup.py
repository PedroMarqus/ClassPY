from app.database.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login varchar(10) NOT NULL,
        senha varchar(10) NOT NULL,
        tipo INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome varchar(50) NOT NULL,
        idade INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        disciplina TEXT,
        nota REAL,
        FOREIGN KEY (aluno_id) REFERENCES alunos(id)
    )
    """)

    conn.commit()
    conn.close()