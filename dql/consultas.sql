SELECT a.nome, p.nome AS plano, m.status
FROM matriculas m
INNER JOIN alunos a ON m.aluno_id = a.id
INNER JOIN planos p ON m.plano_id = p.id;

SELECT a.nome, m.status
FROM alunos a
LEFT JOIN matriculas m ON a.id = m.aluno_id;

SELECT * FROM alunos ORDER BY nome ASC;