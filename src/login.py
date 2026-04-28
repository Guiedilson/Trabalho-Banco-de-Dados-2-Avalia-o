def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "123":
        print("Login realizado com sucesso!\n")
        return True
    else:
        print("Login inválido!")
        return False