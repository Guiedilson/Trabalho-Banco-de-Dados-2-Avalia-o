-- VIEW: relatório consolidado de alunos e suas matrículas
-- Finalidade: apresentar, em uma única consulta, dados do aluno,
-- plano contratado, preço, data de início e situação da matrícula.

CREATE OR REPLACE VIEW vw_alunos_matriculas AS
SELECT
    m.id AS matricula_id,
    a.id AS aluno_id,
    a.nome AS aluno,
    a.email,
    a.telefone,
    p.nome AS plano,
    p.preco,
    m.data_inicio,
    m.status
FROM matriculas m
INNER JOIN alunos a ON a.id = m.aluno_id
INNER JOIN planos p ON p.id = m.plano_id
ORDER BY a.nome;
