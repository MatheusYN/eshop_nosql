# E-Shop Brasil – Aplicação NoSQL com Streamlit e MongoDB

Este projeto foi desenvolvido como parte da disciplina **Banco de Dados Avançado e Big Data**, com o objetivo de integrar tecnologias modernas para manipulação de dados em ambientes escaláveis. A solução utiliza **MongoDB** como banco NoSQL, **Streamlit** para interface interativa e **Docker** para conteinerização.

 Objetivos do Projeto

- Aplicar conceitos de banco de dados NoSQL
- Desenvolver uma interface CRUD funcional e interativa
- Utilizar contêineres para facilitar a implantação
- Gerar uma grande base de dados fictícios com `Faker`

# Tecnologias Utilizadas

- MongoDB
- Python 3.11
- Streamlit
- Docker e Docker Compose
- Faker e tqdm

# Estrutura de Diretórios

.
├── app.py # Aplicação web com Streamlit
├── gerar_dados.py # Script para geração de dados
├── Dockerfile # Define imagem do app
├── docker-compose.yml # Orquestração dos serviços
├── requirements.txt # Dependências Python
└── README.md


# Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/eshop-nosql.git
cd eshop_nosql

# Inicia com o Docker
docker-compose up --build

# Gera os dados com Faker
python gerar_dados.py

# Funcionalidades CRUD

- Criar novos clientes
- Visualizar registros existentes
- Atualizar nome, email e telefone
- Excluir clientes

