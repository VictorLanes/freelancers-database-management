# Freelancers Database Management

Este projeto é uma aplicação simples que gerencia usuários e anúncios de freelancers utilizando **Python** e **SQLite**. Ele utiliza o **Peewee ORM** para modelagem e manipulação do banco de dados.

## 🚀 Funcionalidades

- Criar usuários com campos únicos, como email.
- Criar anúncios vinculados a usuários.
- Listar todos os anúncios com informações detalhadas.
- Relacionamento entre tabelas (um usuário pode ter vários anúncios).
- Consultas SQL executadas diretamente no código.

## 🛠️ Tecnologias Utilizadas

- **Python** (versão 3.8 ou superior)
- **SQLite** (banco de dados local)
- **Peewee ORM** (para interação com o banco de dados)


## 📂 Estrutura do Projeto

```plaintext
projeto/
│
├── database.py       # Configuração do banco de dados e definição dos modelos
├── main.py           # Operações principais (CRUD e exibição de dados)
├── FreeLancers.db    # Arquivo do banco de dados SQLite (gerado automaticamente)
└── README.md         # Documentação do projeto
