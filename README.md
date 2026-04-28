# 🏋️ Sistema de Academia

## 📖 Descrição

Este projeto foi desenvolvido como parte da disciplina de Banco de Dados, com o objetivo de implementar um sistema de gerenciamento de academia utilizando um banco de dados relacional integrado a uma aplicação externa em Python.

O sistema permite o controle de alunos, planos e matrículas, realizando operações de cadastro, atualização, exclusão e consulta de dados (CRUD), além de consultas complexas utilizando JOIN.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- PostgreSQL
- Biblioteca psycopg2
- Git e GitHub
- VS Code

---

## 🗄️ Estrutura do Banco de Dados

O banco de dados é composto por 3 tabelas principais:

- **alunos** → Armazena dados dos alunos
- **planos** → Armazena os planos disponíveis
- **matriculas** → Relaciona alunos com planos

### 🔗 Relacionamentos:
- Um aluno pode ter várias matrículas
- Cada matrícula está vinculada a um plano
- Uso de **Chaves Primárias (PK)** e **Chaves Estrangeiras (FK)**

---

## ⚙️ Funcionalidades do Sistema

- 🔐 Sistema de Login
- ➕ Cadastro de alunos
- 📋 Listagem de alunos
- ✏️ Atualização de dados
- 🗑️ Exclusão de registros
- 🔎 Consulta com INNER JOIN
- 🔎 Consulta com LEFT JOIN
- 📊 Filtros e ordenação

---

## 🧠 Conceitos Aplicados

- DDL (Data Definition Language)
- DML (Data Manipulation Language)
- DQL (Data Query Language)
- CRUD (Create, Read, Update, Delete)
- INNER JOIN e LEFT JOIN
- Modelagem Relacional

---

## 📁 Estrutura do Projeto


---

## 🎥 Vídeo de Demonstração

👉 https://youtu.be/d21k1Sxo0QQ

---

## 📌 Autor

- Nome: Guilherme Edilson De Almeida Cavalcante Soares
- Disciplina: Banco de Dados
- Professor: Anderson Costa

---

## 📎 Observações

Este projeto atende a todos os requisitos propostos, incluindo:
- Modelagem relacional com 3 tabelas
- Uso de chaves primárias e estrangeiras
- Implementação de CRUD
- Integração com aplicação Python
- Consultas com JOIN
