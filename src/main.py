from db import conectar
from login import login

def menu():
    print("\n=== SISTEMA ACADEMIA ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar aluno")
    print("4 - Deletar aluno")
    print("5 - Consultar matrículas (JOIN)")
    print("0 - Sair")

def cadastrar():
    conn = conectar()
    cur = conn.cursor()

    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    cur.execute(
        "INSERT INTO alunos (nome, email, telefone) VALUES (%s, %s, %s)",
        (nome, email, telefone)
    )

    conn.commit()
    conn.close()
    print("Aluno cadastrado!")

def listar():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM alunos ORDER BY nome")
    dados = cur.fetchall()

    for d in dados:
        print(d)

    conn.close()

def atualizar():
    conn = conectar()
    cur = conn.cursor()

    id = input("ID do aluno: ")
    nome = input("Novo nome: ")

    cur.execute(
        "UPDATE alunos SET nome=%s WHERE id=%s",
        (nome, id)
    )

    conn.commit()
    conn.close()
    print("Atualizado!")

def deletar():
    conn = conectar()
    cur = conn.cursor()

    id = input("ID do aluno: ")

    cur.execute("DELETE FROM alunos WHERE id=%s", (id,))
    conn.commit()
    conn.close()

    print("Deletado!")

def consultar_join():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT a.nome, p.nome, m.status
        FROM matriculas m
        INNER JOIN alunos a ON m.aluno_id = a.id
        INNER JOIN planos p ON m.plano_id = p.id
    """)

    dados = cur.fetchall()

    for d in dados:
        print(f"Aluno: {d[0]} | Plano: {d[1]} | Status: {d[2]}")

    conn.close()

if login():
    while True:
        menu()
        op = input("Escolha: ")

        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            atualizar()
        elif op == "4":
            deletar()
        elif op == "5":
            consultar_join()
        elif op == "0":
            break