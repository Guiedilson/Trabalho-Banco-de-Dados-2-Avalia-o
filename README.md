# Sistema Academia — Projeto de Banco de Dados

## Identificação

- **Integrante:** preencher com o nome do aluno
- **Disciplina:** Projeto de Banco de Dados
- **Professor:** Anderson Costa

## Sobre o projeto

Este projeto é a evolução de uma aplicação CRUD de uma academia desenvolvida anteriormente.

A nova versão mantém as operações básicas de cadastro e consulta e integra recursos avançados do PostgreSQL diretamente à aplicação:

- **View:** relatório consolidado de alunos e matrículas;
- **Function:** consulta o valor do plano associado a uma matrícula;
- **Procedure:** atualiza o status de uma matrícula.

O objetivo é demonstrar a integração entre a aplicação Python e recursos de processamento e organização de dados do banco de dados.

## Tecnologias utilizadas

- Python
- PostgreSQL
- psycopg2
- SQL

## Banco de dados

**SGBD:** PostgreSQL

**Principais tabelas:**
- `alunos`
- `planos`
- `matriculas`

**View criada:**
- `vw_alunos_matriculas`

**Function criada:**
- `calcular_valor_matricula(p_matricula_id)`

**Procedure criada:**
- `atualizar_status_matricula(p_matricula_id, p_novo_status)`

## Estrutura do projeto

```text
projeto-academia/
├── database/
│   ├── tables/
│   │   └── schema.sql
│   ├── inserts/
│   │   └── dados.sql
│   ├── views/
│   │   └── alunos_matriculas.sql
│   ├── functions/
│   │   └── calcular_valor_matricula.sql
│   └── procedures/
│       └── atualizar_status_matricula.sql
├── src/
│   ├── config.example.py
│   ├── db.py
│   ├── login.py
│   └── main.py
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

### 1. Criar o banco

No PostgreSQL, crie um banco chamado:

```sql
CREATE DATABASE academia;
```

Depois conecte-se ao banco `academia`.

### 2. Criar as tabelas

Execute:

```text
database/tables/schema.sql
```

### 3. Inserir dados de teste

Execute:

```text
database/inserts/dados.sql
```

### 4. Criar a View

Execute:

```text
database/views/alunos_matriculas.sql
```

### 5. Criar a Function

Execute:

```text
database/functions/calcular_valor_matricula.sql
```

### 6. Criar a Procedure

Execute:

```text
database/procedures/atualizar_status_matricula.sql
```

### 7. Configurar o Python

Dentro de `src/`, copie:

```text
config.example.py
```

para:

```text
config.py
```

Depois informe sua senha do PostgreSQL em `config.py`.

### 8. Instalar a dependência

No terminal:

```bash
python -m pip install -r requirements.txt
```

### 9. Executar

Entre na pasta `src`:

```bash
cd src
python main.py
```

### Login

```text
Usuário: admin
Senha: 123
```

## Funcionalidades do projeto

### CRUD

- Cadastro de aluno
- Listagem de alunos
- Atualização de aluno
- Exclusão de aluno
- Consulta de matrículas

### View

A opção **6 - Relatório de matrículas (VIEW)** consulta a `vw_alunos_matriculas`.

Ela consolida dados de `alunos`, `planos` e `matriculas`, evitando que a aplicação precise montar novamente esse relacionamento.

### Function

A opção **7 - Consultar valor da matrícula (FUNCTION)** executa:

```sql
SELECT calcular_valor_matricula(id);
```

A Function recebe o ID da matrícula e retorna o valor do plano associado.

### Procedure

A opção **8 - Alterar status da matrícula (PROCEDURE)** executa:

```sql
CALL atualizar_status_matricula(id, 'Ativa');
```

A Procedure valida o novo status e atualiza a matrícula.

## Ordem recomendada para demonstração

1. Fazer login.
2. Mostrar o cadastro/listagem de alunos.
3. Abrir a opção de relatório e demonstrar a **View**.
4. Informar o ID de uma matrícula e demonstrar a **Function**.
5. Alterar o status de uma matrícula e demonstrar a **Procedure**.
6. Voltar ao relatório para mostrar o resultado da alteração.

## Observação sobre segurança

A senha do PostgreSQL não fica no código principal nem deve ser publicada no GitHub. O arquivo `src/config.py` é ignorado pelo Git e deve ser configurado localmente.


### Configuração local

Crie `src/config.py` a partir de `src/config.example.py` e informe os dados do PostgreSQL local. O arquivo `config.py` está no `.gitignore` e não deve ser enviado ao GitHub.
