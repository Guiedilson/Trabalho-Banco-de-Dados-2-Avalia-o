-- Criação das tabelas do Sistema Academia
-- Banco: PostgreSQL

CREATE TABLE IF NOT EXISTS alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS planos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0)
);

CREATE TABLE IF NOT EXISTS matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INT NOT NULL,
    plano_id INT NOT NULL,
    data_inicio DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Ativa',
    CONSTRAINT matriculas_aluno_fk
        FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    CONSTRAINT matriculas_plano_fk
        FOREIGN KEY (plano_id) REFERENCES planos(id),
    CONSTRAINT matriculas_status_ck
        CHECK (status IN ('Ativa', 'Inativa', 'Pendente'))
);
