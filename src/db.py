import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="academia",
        user="postgres",
        password="1234"
    )