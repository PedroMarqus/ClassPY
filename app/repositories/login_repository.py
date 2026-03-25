from app.database.connection import get_connection

def login_usuario(login, senha):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE login = ? AND senha = ?",
        (login, senha)
    )
    user = cursor.fetchone()

    conn.close()
    return user