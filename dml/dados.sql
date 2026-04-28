INSERT INTO alunos (nome, email, telefone) VALUES
('Carlos Silva', 'carlos@email.com', '99999-1111'),
('Ana Souza', 'ana@email.com', '99999-2222');

INSERT INTO planos (nome, preco) VALUES
('Mensal', 100.00),
('Trimestral', 270.00);

INSERT INTO matriculas (aluno_id, plano_id, data_inicio, status) VALUES
(1, 1, '2026-01-10', 'Ativa'),
(2, 2, '2026-02-15', 'Ativa');