-- PROCEDURE: atualiza a situação de uma matrícula.
-- Finalidade: centralizar no banco a alteração do status de uma matrícula.

CREATE OR REPLACE PROCEDURE atualizar_status_matricula(
    p_matricula_id INT,
    p_novo_status VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_novo_status NOT IN ('Ativa', 'Inativa', 'Pendente') THEN
        RAISE EXCEPTION
            'Status inválido. Use: Ativa, Inativa ou Pendente.';
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM matriculas WHERE id = p_matricula_id
    ) THEN
        RAISE EXCEPTION 'Matrícula % não encontrada.', p_matricula_id;
    END IF;

    UPDATE matriculas
       SET status = p_novo_status
     WHERE id = p_matricula_id;
END;
$$;
