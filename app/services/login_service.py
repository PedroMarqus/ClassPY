from app.repositories import login_repository

def login_usuario(login, senha):
    if not login or not senha:
        raise ValueError("Login e senha são obrigatórios")

    user = login_repository.login_usuario(login, senha)
    if not user:
        raise ValueError("Login ou senha inválidos")

    return user