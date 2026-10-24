# Sistema de Controle de Ponto — planejamento

## Objetivo

Planejar um sistema didático para registrar jornadas de trabalho e gerar relatórios de horas. A primeira versão será um projeto de aprendizagem, não um sistema pronto para uso comercial ou para cumprir obrigações legais trabalhistas.

## Escopo inicial

- Cadastrar funcionários com identificadores fictícios.
- Registrar entrada, início e fim de intervalo e saída.
- Consultar registros por funcionário e período.
- Calcular duração diária a partir de registros válidos.
- Gerar relatório de horas por período.

## Tecnologias planejadas

- Python para regras de negócio.
- SQL para persistência dos dados.
- Testes para validar cálculos e casos incompletos.

## Modelo inicial

O arquivo [`schema.sql`](./schema.sql) apresenta um esquema de partida para funcionários e marcações. Ele precisa ser revisado e testado no SGBD escolhido antes de ser usado.

## Etapas

1. Definir regras de cálculo e tratamento de marcações incompletas.
2. Criar e testar o banco de dados.
3. Implementar cadastro e registro de marcações.
4. Criar consultas e relatórios.
5. Adicionar testes, documentação e exemplos fictícios.

## Cuidados

Não usar dados reais de funcionários. Um produto real exigiria análise de requisitos legais, segurança, auditoria, controle de acesso, backups e tratamento de dados pessoais.

**Status:** planejamento inicial; ainda não é uma aplicação funcional.
