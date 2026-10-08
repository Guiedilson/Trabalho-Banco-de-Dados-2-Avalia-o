# Roteiro do vídeo — Projeto de Banco de Dados

## 1. Apresentação

"Olá, meu nome é [NOME]. Este é o projeto da disciplina Projeto de Banco de Dados, ministrada pelo professor Anderson Costa.

O projeto consiste em um sistema de academia desenvolvido em Python com PostgreSQL. A aplicação começou como um CRUD e foi evoluída para utilizar recursos avançados do banco de dados: View, Function e Procedure."

## 2. Mostrar a aplicação

"Esta é a tela principal do sistema. Primeiro fazemos o login e depois temos as opções de cadastro, consulta e atualização dos alunos e matrículas."

## 3. View

"Agora vou demonstrar a View. A View `vw_alunos_matriculas` foi criada para consolidar informações das tabelas alunos, planos e matriculas.

Na aplicação, a opção 6 consulta diretamente essa View e apresenta o relatório de matrículas."

## 4. Function

"Agora vou demonstrar a Function. A `calcular_valor_matricula` recebe o ID de uma matrícula e retorna o valor do plano associado a ela.

A aplicação executa essa Function diretamente no PostgreSQL e apresenta o resultado."

## 5. Procedure

"Por último, temos a Procedure `atualizar_status_matricula`. Ela recebe o ID da matrícula e o novo status, valida o valor informado e realiza a atualização no banco.

A aplicação chama a Procedure pela opção 8."

## 6. Funcionamento integrado

"Neste projeto, os recursos não foram criados apenas para cumprir o requisito. Eles estão integrados às funcionalidades da aplicação.

A aplicação chama o banco, o banco executa a View, Function ou Procedure e o resultado retorna para a aplicação."

## 7. Encerramento

"Com isso, demonstramos a evolução de um CRUD simples para uma aplicação com maior integração entre Python e PostgreSQL, utilizando recursos para consultar, processar e atualizar dados."
