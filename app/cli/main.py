from app.services import login_service, aluno_service, users_service, nota_service
from app.database.setup import create_tables

create_tables()

while True:
    print("-------- ClassPY -------- ")
    print("| 1 - Entrar |")
    print("| 2 - Sobre nós   |")
    print("| 3 - Sair   |")
    print("-------------------------")
    texto = input("Digite uma opção: ")
    if texto == "1":
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        user = login_service.login_usuario(login, senha)
        if user:
            if user["tipo"] == 0:
                while True:
                    print("Bem-vindo ao painel de controle!")
                    print("1 - Ver usuários")
                    print("2 - Apagar usuários")
                    print("3 - Criar usuários")
                    print("4 - Editar usuários") #ainda tem q fazer
                    print("5 - Sair")
                    opcao = input("Digite uma opção: ")
                    if opcao == "1":
                        print("Listando usuários...")
                        usuarios = users_service.listar_usuarios_service()
                        for usuario in usuarios:
                            print("ID: {}, Login: {}, Tipo: {}".format(usuario[0], usuario[1], usuario[3]))
                    elif opcao == "2":
                        id = input("Digite o ID do usuário a ser apagado: ")
                        print("apagando usuário com id {}...".format(id))
                        users_service.deletar_usuario_service(id)
                    elif opcao == "3":
                        nome = input("Digite o nome do usuário: ")
                        senha = input("Digite a senha do usuário: ")
                        tipo = input("Digite o tipo do usuário (0 para admin, 1 para user)")
                        print("Criando usuário...")
                        users_service.criar_usuario_service(nome, senha, tipo)
                    elif opcao == "4":
                        id = input("Digite o ID do usuário a ser editado: ")
                        print("Deixando em branco os campos que não deseja editar")
                        nome = input("Digite o novo nome do usuário: ")
                        senha = input("Digite a nova senha do usuário: ")
                        tipo = input("Digite o novo tipo do usuário (0 para admin, 1 para user)")
                        print("Editando usuário com id {}...".format(id))
                        users_service.editar_usuario_service(id, nome if nome else None, senha if senha else None, tipo if tipo else None)
                    elif opcao == "5":
                        print("Saindo do painel de controle...")
                        break
                    else:
                        print("Opção inválida")
            elif user["tipo"] == 1:
                while True:
                    print("Bem-vindo ao painel de controle!")
                    print("1 - Ver perfil")
                    print("2 - Ver alunos")
                    print("3 - Criar aluno")
                    print("4 - Buscar aluno por nome")
                    print("5 - Criar nota para aluno")
                    print("6 - Ver todas as notas ")
                    print("7 - Sair")
                    opcao = input("Digite uma opção: ")
                    if opcao == "1":
                        print("Perfil do usuário:")
                        print("Login: {}".format(user["login"]))
                        print("Tipo: {}".format(user["tipo"]))
                    elif opcao == "2":
                        print("Listando alunos...")
                        alunos = aluno_service.listar_alunos()
                        for aluno in alunos:
                            print("ID: {}, Nome: {}, Idade: {}".format(aluno[0], aluno[1], aluno[2]))
                    elif opcao == "3":
                        nome = input("Digite o nome do aluno: ")
                        idade = input("Digite a idade do aluno: ")
                        print("Criando aluno...")
                        aluno_service.criar_aluno(nome, idade)
                    elif opcao == "4":
                        nome = input("Digite o nome do aluno: ")
                        print("Buscando aluno por nome...")
                        alunos = aluno_service.buscar_aluno_por_nome(nome)
                        for aluno in alunos:
                            print("ID: {}, Nome: {}, Idade: {}".format(aluno[0], aluno[1], aluno[2]))
                    elif opcao == "5":
                        aluno_id = input("Digite o ID do aluno: ")
                        disciplina = input("Digite a disciplina: ")
                        nota = input("Digite a nota: ")
                        print("Criando nota para aluno...")
                        nota_service.criar_nota(aluno_id, disciplina, nota)
                    elif opcao == "6":
                        print("Listando todas as notas...")
                        notas = nota_service.listar_notas()
                        for nota in notas:
                            print("ID: {}, Aluno ID: {}, Nome: {}, Disciplina: {}, Nota: {}".format(nota[0], nota[1], nota[2], nota[3], nota[4]))
                    elif opcao == "7":
                        print("Saindo do painel de controle...")
                        break
        else:
            print("Login ou senha incorretos!")
    elif texto == "2":
        print("Nós do ClassPY fomos criados para validar conhecimentos em Python, e somos uma empresa fícticia")
    elif texto == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida")