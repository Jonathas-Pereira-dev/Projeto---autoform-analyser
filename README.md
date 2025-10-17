# Projeto---autoform-analyser


O AutoForm Analyser tem como objetivo coletar e analisar dados de formulários automaticamente, criando uma aplicação web onde o operador registra os dados definidos pelo desenvolvedor.
O sistema então preenche automaticamente uma planilha principal com os testes realizados, facilitando o controle e automação do processo.

⚙️ Tecnologias Utilizadas

Python (versão 3.12 ou compatível)

FastAPI — Framework backend para APIs modernas e rápidas

PostgreSQL — Banco de dados relacional

SQLAlchemy / Alembic — ORM e controle de migrações

Pandas — Manipulação de dados e planilhas

Frontend (futuro) — HTML, CSS, JS (ou React)
 
🗄️ Estrutura de Dados

Os dados preenchidos pelos operadores são armazenados no PostgreSQL, organizados por:

Informações do formulário

Resultados dos testes realizados

Metadados do operador e do desenvolvedor