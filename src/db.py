import psycopg2

try:
    from config import DB_CONFIG
except ImportError:
    raise RuntimeError(
        "Crie o arquivo src/config.py a partir de src/config.example.py "
        "e informe a senha do PostgreSQL."
    )


def conectar():
    """Abre uma conexão com o PostgreSQL usando a configuração local."""
    config = dict(DB_CONFIG)
    # 127.0.0.1 evita problemas de resolução/localização do localhost no Windows.
    if config.get("host") == "localhost":
        config["host"] = "127.0.0.1"

    try:
        return psycopg2.connect(**config)
    except UnicodeDecodeError as erro:
        raise RuntimeError(
            "Não foi possível interpretar a mensagem do PostgreSQL. "
            "Verifique a senha do usuário postgres e se o servidor PostgreSQL "
            "está ativo em 127.0.0.1:5432. "
            f"Detalhe técnico: {erro}"
        ) from erro
