Configuração do Ambiente

    Arquivo .env:
        Este projeto utiliza um arquivo .env para determinar se o ambiente é de produção ou de teste.
        A variável de ambiente ENV deve ser definida como prod para produção ou test para o ambiente de testes.
        Para definir a variável, você pode adicionar a seguinte linha ao seu arquivo .env:

        makefile

    ENV=prod

Dependências:

    Este projeto utiliza as seguintes dependências, que podem ser instaladas através do Poetry:

    bash

        poetry install

Execução de Testes

Para executar os testes do projeto, utilize o pytest. O pytest irá automaticamente buscar por arquivos que começam com test_ ou terminam com _test e executar os testes definidos.

Para executar os testes, use o seguinte comando:

bash

poetry run pytest

Rotas da API

As seguintes rotas estão disponíveis na API:

    GET /users/: Retorna todos os usuários.
    GET /users/{id}: Retorna um usuário específico pelo ID.
    POST /register: Registra um novo usuário. Retorna um erro se o email já estiver registrado.
    PUT /users/{id}: Atualiza as informações de um usuário existente.
    DELETE /users/{id}: Remove um usuário pelo ID.

Observações

    Certifique-se de que o MongoDB esteja em execução na máquina local para que a aplicação possa se conectar ao banco de dados.
    A estrutura de usuários é baseada no modelo definido no arquivo models/user.py.