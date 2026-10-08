from db import conectar
from login import login


def menu():
    print("\n=== SISTEMA ACADEMIA ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar aluno")
    print("4 - Deletar aluno")
    print("5 - Consultar matrículas (JOIN)")
    print("6 - Relatório de matrículas (VIEW)")
    print("7 - Consultar valor da matrícula (FUNCTION)")
    print("8 - Alterar status da matrícula (PROCEDURE)")
    print("0 - Sair")


def cadastrar():
    conn = conectar()
    cur = conn.cursor()
    try:
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")

        cur.execute(
            "INSERT INTO alunos (nome, email, telefone) VALUES (%s, %s, %s)",
            (nome, email, telefone)
        )
        conn.commit()
        print("Aluno cadastrado!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao cadastrar: {erro}")
    finally:
        cur.close()
        conn.close()


def listar():
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, nome, email, telefone FROM alunos ORDER BY nome")
        dados = cur.fetchall()

        print("\n--- ALUNOS ---")
        if not dados:
            print("Nenhum aluno cadastrado.")
        for d in dados:
            print(f"ID: {d[0]} | Nome: {d[1]} | Email: {d[2]} | Telefone: {d[3]}")
    finally:
        cur.close()
        conn.close()


def atualizar():
    conn = conectar()
    cur = conn.cursor()
    try:
        id_aluno = input("ID do aluno: ")
        nome = input("Novo nome: ")

        cur.execute(
            "UPDATE alunos SET nome=%s WHERE id=%s",
            (nome, id_aluno)
        )

        if cur.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            conn.commit()
            print("Aluno atualizado!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao atualizar: {erro}")
    finally:
        cur.close()
        conn.close()


def deletar():
    conn = conectar()
    cur = conn.cursor()
    try:
        id_aluno = input("ID do aluno: ")
        cur.execute("DELETE FROM alunos WHERE id=%s", (id_aluno,))

        if cur.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            conn.commit()
            print("Aluno deletado!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao deletar: {erro}")
    finally:
        cur.close()
        conn.close()


def consultar_join():
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT a.nome, p.nome, m.status
            FROM matriculas m
            INNER JOIN alunos a ON m.aluno_id = a.id
            INNER JOIN planos p ON m.plano_id = p.id
            ORDER BY a.nome
            """
        )

        dados = cur.fetchall()
        print("\n--- MATRÍCULAS ---")
        for d in dados:
            print(f"Aluno: {d[0]} | Plano: {d[1]} | Status: {d[2]}")
    finally:
        cur.close()
        conn.close()


def consultar_view():
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT matricula_id, aluno, plano, preco, data_inicio, status
            FROM vw_alunos_matriculas
            """
        )
        dados = cur.fetchall()

        print("\n--- RELATÓRIO DE MATRÍCULAS (VIEW) ---")
        if not dados:
            print("Nenhuma matrícula encontrada.")
        for d in dados:
            print(
                f"Matrícula: {d[0]} | Aluno: {d[1]} | "
                f"Plano: {d[2]} | Valor: R$ {d[3]:.2f} | "
                f"Início: {d[4]} | Status: {d[5]}"
            )
    finally:
        cur.close()
        conn.close()


def consultar_function():
    conn = conectar()
    cur = conn.cursor()
    try:
        id_matricula = input("ID da matrícula: ")
        cur.execute(
            "SELECT calcular_valor_matricula(%s)",
            (id_matricula,)
        )
        valor = cur.fetchone()[0]
        print(f"Valor do plano da matrícula: R$ {valor:.2f}")
    except Exception as erro:
        print(f"Erro ao consultar a Function: {erro}")
    finally:
        cur.close()
        conn.close()


def atualizar_status_procedure():
    conn = conectar()
    cur = conn.cursor()
    try:
        id_matricula = input("ID da matrícula: ")
        print("Status disponíveis: Ativa | Inativa | Pendente")
        novo_status = input("Novo status: ").strip()

        cur.execute(
            "CALL atualizar_status_matricula(%s::INT, %s::VARCHAR)",
            (id_matricula, novo_status)
        )
        conn.commit()
        print("Status da matrícula atualizado pela Procedure!")
    except Exception as erro:
        conn.rollback()
        print(f"Erro ao executar a Procedure: {erro}")
    finally:
        cur.close()
        conn.close()


def executar():
    if not login():
        return

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
        elif op == "6":
            consultar_view()
        elif op == "7":
            consultar_function()
        elif op == "8":
            atualizar_status_procedure()
        elif op == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar()

