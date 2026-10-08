def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "123":
        print("\nLogin realizado com sucesso!\n")
        return True

    print("\nLogin inválido!\n")
    return False
