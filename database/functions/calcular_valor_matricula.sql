-- FUNCTION: retorna o valor do plano associado a uma matrícula.
-- Finalidade: realizar um cálculo/consulta no banco e disponibilizar
-- o resultado para a aplicação.

CREATE OR REPLACE FUNCTION calcular_valor_matricula(p_matricula_id INT)
RETURNS NUMERIC(10,2)
LANGUAGE plpgsql
AS $$
DECLARE
    v_valor NUMERIC(10,2);
BEGIN
    SELECT p.preco
      INTO v_valor
      FROM matriculas m
      INNER JOIN planos p ON p.id = m.plano_id
     WHERE m.id = p_matricula_id;

    IF v_valor IS NULL THEN
        RAISE EXCEPTION 'Matrícula % não encontrada.', p_matricula_id;
    END IF;

    RETURN v_valor;
END;
$$;
