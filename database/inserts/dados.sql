-- Dados de teste do Sistema Academia

INSERT INTO alunos (nome, email, telefone)
VALUES
    ('Carlos Silva', 'carlos@email.com', '99999-1111'),
    ('Ana Souza', 'ana@email.com', '99999-2222')
ON CONFLICT (email) DO NOTHING;

INSERT INTO planos (nome, preco)
SELECT 'Mensal', 100.00
WHERE NOT EXISTS (SELECT 1 FROM planos WHERE nome = 'Mensal');

INSERT INTO planos (nome, preco)
SELECT 'Trimestral', 270.00
WHERE NOT EXISTS (SELECT 1 FROM planos WHERE nome = 'Trimestral');

INSERT INTO matriculas (aluno_id, plano_id, data_inicio, status)
SELECT a.id, p.id, DATE '2026-01-10', 'Ativa'
FROM alunos a, planos p
WHERE a.email = 'carlos@email.com' AND p.nome = 'Mensal'
  AND NOT EXISTS (
      SELECT 1 FROM matriculas m
      WHERE m.aluno_id = a.id AND m.plano_id = p.id
  );

INSERT INTO matriculas (aluno_id, plano_id, data_inicio, status)
SELECT a.id, p.id, DATE '2026-02-15', 'Ativa'
FROM alunos a, planos p
WHERE a.email = 'ana@email.com' AND p.nome = 'Trimestral'
  AND NOT EXISTS (
      SELECT 1 FROM matriculas m
      WHERE m.aluno_id = a.id AND m.plano_id = p.id
  );
