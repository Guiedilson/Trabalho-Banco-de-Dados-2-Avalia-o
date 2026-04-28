CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE planos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INT,
    plano_id INT,
    data_inicio DATE,
    status VARCHAR(20),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (plano_id) REFERENCES planos(id)
);