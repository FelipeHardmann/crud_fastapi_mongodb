Projeto CRUD com MongoDB usando FastAPI

Este projeto implementa uma API CRUD usando FastAPI e MongoDB como banco de dados, com gerenciamento de dependências usando Poetry.
Pré-requisitos

    Python 3.11 ou superior
    MongoDB em execução localmente ou em uma instância acessível (ex: MongoDB Atlas)
    Poetry para gerenciamento de dependências

Instalação do Poetry

Para instalar o Poetry, use o seguinte comando:

bash

curl -sSL https://install.python-poetry.org | python3 -

Clonando o repositório

Clone este repositório para sua máquina:

bash

git clone https://github.com/FelipeHardmann/crud_fastapi_mongodb.git
cd crud_fastapi_mongodb

Instalando as Dependências

Use o Poetry para instalar todas as dependências do projeto:

bash

poetry install

Este comando cria um ambiente virtual isolado e instala todas as bibliotecas necessárias, conforme especificado no arquivo pyproject.toml.
Configuração do Banco de Dados

Certifique-se de que você possui um banco MongoDB em execução. Por padrão, o MongoDB local roda em mongodb://localhost:27017. Caso esteja usando uma URL diferente, altere a conexão no código da aplicação.
Executando o Servidor

Para iniciar o servidor, use o Uvicorn, que é um servidor ASGI leve recomendado para FastAPI. Execute o comando:

bash

poetry run uvicorn main:app --reload

Aqui:

    main:app é o caminho para a aplicação FastAPI.
    --reload ativa o recarregamento automático durante o desenvolvimento.

Testando a API

Uma vez que o servidor esteja em execução, você pode acessar a documentação da API na interface interativa do Swagger em:

arduino

http://127.0.0.1:8000/docs

Ou a documentação alternativa em formato Redoc:

arduino

http://127.0.0.1:8000/redoc

Estrutura do Projeto

    main.py: Arquivo principal que define a aplicação FastAPI e as rotas.
    pyproject.toml: Configuração das dependências gerenciadas pelo Poetry.

Autenticação e Segurança

A biblioteca bcrypt é utilizada para hashing de senhas, e o Pydantic auxilia na validação dos dados.
Contribuição

Para contribuir, faça um fork do repositório, crie um branch com as suas alterações e abra um pull request.
