-- Consultas rápidas para testar os recursos após a instalação.

-- Testar a View
SELECT * FROM vw_alunos_matriculas;

-- Testar a Function
SELECT calcular_valor_matricula(1);

-- Testar a Procedure
CALL atualizar_status_matricula(1, 'Inativa');

-- Conferir o resultado
SELECT * FROM vw_alunos_matriculas WHERE matricula_id = 1;
