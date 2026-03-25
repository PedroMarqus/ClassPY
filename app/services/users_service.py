from app.repositories.users_repository import criar_usuario, listar_usuarios, deletar_usuario, editar_usuario

def criar_usuario_service(login, senha, tipo):
    if login is None or senha is None or tipo is None:
        raise ValueError("Login, senha e tipo são obrigatórios")

    criar_usuario(login, senha, tipo)

def listar_usuarios_service():
    return listar_usuarios()

def deletar_usuario_service(user_id):
    if not user_id:
        raise ValueError("ID do usuário é obrigatório")

    deletar_usuario(user_id)

def editar_usuario_service(user_id, login=None, senha=None, tipo=None):
    if user_id is None:
        raise ValueError("ID do usuário é obrigatório")

    if login is None and senha is None and tipo is None:
        raise ValueError("Pelo menos um campo (login, senha ou tipo) deve ser fornecido para edição")

    editar_usuario(user_id, login, senha, tipo)