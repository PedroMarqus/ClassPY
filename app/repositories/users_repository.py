from app.database.connection import get_connection

def criar_usuario(login, senha, tipo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (login, senha, tipo) VALUES (?, ?, ?)",
        (login, senha, tipo)
    )

    conn.commit()
    conn.close()

def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios

def deletar_usuario(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

    conn.commit()
    conn.close()

def editar_usuario(user_id, login=None, senha=None, tipo=None):
    conn = get_connection()
    cursor = conn.cursor()

    if login is not None:
        cursor.execute("UPDATE users SET login = ? WHERE id = ?", (login, user_id))
    if senha is not None:
        cursor.execute("UPDATE users SET senha = ? WHERE id = ?", (senha, user_id))
    if tipo is not None:
        cursor.execute("UPDATE users SET tipo = ? WHERE id = ?", (tipo, user_id))

    conn.commit()
    conn.close()