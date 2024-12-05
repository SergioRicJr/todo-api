## To do Project

Este projeto é uma API com uma proposta de gerenciar atividades/tarefas a fazer, tipos de atividades e usuários. Porém, o seu diferencial está na qualidade e detalhes de seu desenvolvimento, com sistema de mensageria para confirmação de Email de usuários, gestão de métricas, logs e traces da aplicação com uma stack completa e moderna de observabilidade, pipeline de CI (Integração contínua), documentação de alto nível com Swagger, exemplos e testes manuais com Postman, testes unitários e de integração, padrão de commit, uso do gitflow e muito mais...

## Tabela de conteúdos
* [Funcionalidades](#funcionalidades)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos para uso](#requisitos-para-uso)
* [Instalação](#instalação)
* [Como iniciar](#como-iniciar)
    * [Aplicação BackEnd](#aplicacao-fastapi)
    * [Pacote de observabilidade](#pacote-de-observabilidade)
    * [Aplicação para envio de email](#aplicacao-para-envio-de-email)
* [Como usar](#como-usar)
    * [Aplicação BackEnd](#aplicacao-fastapi)
        * [Postman](#postman)
        * [Admin](#admin)
        * [Swagger](#swagger)
    * [Pacote de observabilidade](#pacote-de-observabilidade)
* [Informações adicionais](#informacoes-adicionais)
    * [Confirmação de email](#confirmacao-de-email)
    * [DER (Diagrama Entidade Relacionamento)](#Der-(Diagrama-Entidade-Relacionamento))

## Funcionalidades

- [x] Login
- [x] Logout
- [x] Refresh token
- [x] Criar usuário
- [x] Listar, filtrar e buscar usuários
- [x] Resgatar um usuário
- [x] Alterar usuário
- [x] Deletar usuário
- [x] Confirmar email
- [x] Criar tipo de tarefa
- [x] Listar, filtrar e buscar tipo de tarefa
- [x] Resgatar um tipo de tarefa
- [x] Alterar tipo de tarefa
- [x] Deletar tipo de tarefa
- [x] Criar tarefa
- [x] Listar, filtrar e buscar tarefa
- [x] Resgatar uma tarefa
- [x] Alterar tarefa
- [x] Deletar tarefa

##  🛠  Tecnologias utilizadas

- Python: 3.11.4 (bibliotecas em requirements.txt)
- PostgreSql: 13.9 
- Docker : 24.0.6
- Docker-compose: v2.20.2
- RabbitMQ 3.12
- Grafana
- NGINX
- Prometheus
- Pushgateway
- Tempo
- Loki
- Postman

## Requisitos para uso

## Instalação

- **Clone o repositório:** Abra o prompt de comando ou terminal e digite o seguinte código:

```
    git clone https://github.com/SergioRicJr/todo-api
```

- **Navegue até a pasta do projeto**
```
    cd todo-api
```

- **Abra a IDE:** Para editar e rodar o código utilize uma IDE, a mais recomendada é o Visual Studio Code. Utilize o seguinte comando no terminal:

```
    code .
```

- **Altere as variáveis de ambiente necessárias da aplicação principal:** O arquivo .env está na pasta main_app. Lá você terá as seguintes variáveis:

```

    # key used by Django to manage security issues in our application
    SECRET_KEY="todo1vgi=2jv=z@r1pq6a1i&zn7wah=%dh1xcg5$v&9&5j1!@6o+3u" 

    # Enables or disables debug mode that brings application logs to the terminal. In production, set it to 0
    DEBUG="1" 

    # configures the engine used for the database
    DB_ENGINE="django.db.backends.postgresql" 

    # defines the database host. Using docker compose, this is the name of the database service chosen in the .yaml file
    POSTGRES_HOST="psql" 
    
    # configure the database user password
    POSTGRES_PASSWORD="bHkH242GdlkgVXMtGWKrGV96iL8F5-Dw" 

    # configures the database user name
    POSTGRES_USER="postgres" 

    # defines the name of the default database to be created and used
    POSTGRES_DB="dbtodo" 

    # defines the port on which the database will be accessed
    PGPORT="5432" 

    # define whether you want to run using the previously specified database or ignore it and use sqlite
    SQLITE="1" 

    PROMETHEUS_URL=nginx:80/pushgateway
    LOKI_URL=http://nginx:80/loki/api/v1/push

    ROUTING_KEY=D14A028C2A3A2BC947
    IP_RABBITMQ="rabbitmq"
    RABBIT_USERNAME="admin"
    RABBIT_PASSWORD="admin"

    # configures the data of the super user to be created initially
    SUPERUSER_NAME="admin"
    SUPERUSER_USERNAME="admin"
    SUPERUSER_EMAIL="admin@gmail.com"
    SUPERUSER_PASSWORD="admin"

```

- **Altere as variáveis de ambiente necessárias da aplicação de envio de email:** O arquivo .env está na pasta email_sender. Lá você terá as seguintes variáveis:

```
    ROUTING_KEY=D14A028C2A3A2BC947
    EMAIL="your email"
    EMAIL_PASSWORD="your email app password"

    # RabbitMQ credentials
    USERNAME="admin"
    PASSWORD="admin"    
```

## Como iniciar

Antes de iniciar certifique-se de estar com o Docker ativo.

- **Pacote de observabilidade**

    - Naveque até a pasta do pacote de observabilidade:

    ```
        cd observability
    ```

    - Inicie utilizando o Docker-compose:

    ```
        docker-compose up
    ```
- **Aplicação BackEnd**
    - Naveque até a pasta da API:

    ```
        cd main_app
    ```

    - Inicie utilizando o Docker-compose:

    ```
        docker-compose up
    ```  

- **Aplicação para envio de email**
    - Naveque até a pasta da apliação de envio de email:

    ```
        cd email_sender
    ```

    - Inicie utilizando o Docker-compose:

    ```
        docker-compose up
    ```   

## Como usar

Após todos os componentes da aplicação estarem ativos, você pode testar e utilizar seguindo os passos a seguir.

### Aplicação BackEnd

É possível testar, ter exemplos de uso e acessar a partes da aplicação BackEnd através de 3 formas.

#### Postman

O Postman é uma ferramenta de desenvolvimento que facilita o trabalho com APIs (Interface de Programação de Aplicações). Ele é amplamente utilizado por desenvolvedores para testar, documentar e interagir com APIs, tornando o processo de desenvolvimento e depuração mais eficiente. 

Para fazer requisições a essa API, você deve abrir o aplicativo do Postman, e apertar o botão para importar collections.

![Import collection no postman](./images/postman_import.png)

Agora basta selecionar o arquivo 'todo_collection.postman_collection.json' que está na pasta raiz do projeto.

#### Admin

A API tem uma área de Admin com interface gráfica que pode ser acessado através da url `http://127.0.0.1/admin`, é possível acessar passando as credenciais utilizadas no .env que criaram o super usuário. No admin é possível manipular todos os registros do banco de dados de forma intuitiva.

![Django admin](./images/django_admin.png)


#### Swagger

Uma vez logado no Admin, é possível acessar o Swagger, que traz exemplos de resposta de todos os endpoints, os schemas, tipos de dados, e permite realizar requisições e testes manuais. Esse serviço ficará disponível na url `http://127.0.0.1/swagger`.

- Após entrar na página do swagger, é necessário fazer a autenticação através do endpoint `/auth/login` passando usuário e senha. Na resposta você receberá um token de acesso e um refresh token da seguinte forma:

```
    {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTU5Njc2MCwiaWF0IjoxNzE5NTEwMzYwLCJqdGkiOiJhZDQ2ZDQ3ZDlmZjc0Mjg0YTI3YmU5NGU1ODVlNTBjZCIsInVzZXJfaWQiOjF9.3krpN8hkesg3f7wBzrQMDSSPr23j1sC1x0AyTbOvSVw",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NTE3NTYwLCJpYXQiOjE3MTk1MTAzNjAsImp0aSI6Ijk1YjI5ZWZmOWYzMTQ1N2Y5MTRjMDEzZGE3MmQzMDkxIiwidXNlcl9pZCI6MX0.fBbwCvrjN4hGuT9IauhVxnqp2uwT7PJyR3rtQY-3y1Q"
    }
```

- pegue o valor da chave `access` e adicione no value do authorize dessa forma "Bearer {access-token}":

![Interface do swagger botão authorize](./images/swagger_authorize.png)

Agora você tem acesso aos demais endpoints.

### Pacote de observabilidade

O pacote de observabilidade permite que as informações de métricas, traces e logs geradas pela aplicação sejam visualizadas através dos gráficos no Grafana que está disponível na url `http://127.0.0.1/grafana`. Para mais informações sobre o uso e funcionamento do pacote de observabilidade, você pode acessar este [repositório](https://github.com/SergioRicJr/observability-package). 

Caso tenha interesse em conhecer mais sobre a configuração da API para se conectar e trocar informações com as ferramentas Prometheus, PushGateway, Loki e tempo, você pode acessar o repoitório da [biblioteca observability-mtl-instrument](https://github.com/SergioRicJr/observability-mtl-instrument), que foi desenvolvida por mim e utilizada nesse projeto.

Aqui está uma sugestão de README explicando sobre testes unitários e de integração, sua importância, como eles funcionam no seu projeto e como executá-los usando `pytest`.

---

## Documentação de Testes

### Introdução

Este projeto utiliza **testes unitários** e **testes de integração** para garantir a qualidade do código, verificar a integridade das funcionalidades e evitar a introdução de bugs em novas implementações.

#### O que são Testes Unitários?
Os **testes unitários** verificam o comportamento de unidades isoladas de código, como funções, métodos ou classes. Eles asseguram que cada componente do sistema funcione conforme o esperado, independentemente de outros componentes.

**Benefícios:**
- Facilitam a identificação de erros em partes específicas do código.
- Servem como documentação viva do comportamento esperado.
- Aumentam a confiabilidade do sistema ao garantir a estabilidade das unidades.

#### O que são Testes de Integração?
Os **testes de integração** verificam se diferentes módulos ou componentes do sistema funcionam corretamente quando integrados. Eles testam o fluxo de dados entre diferentes partes da aplicação.

**Benefícios:**
- Garantem que os módulos funcionem em conjunto como esperado.
- Detectam problemas que podem surgir devido à comunicação entre componentes.
- Simulam cenários reais de uso da aplicação.

---

### Estrutura de Testes no Projeto

#### Arquivos de Teste

- **`taskFactory.py`**: Define uma fábrica de objetos para criar usuários fictícios usados nos testes.
- **`conftest.py`**: Configura fixtures para o ambiente de testes, incluindo cliente de API, autenticação e criação de usuários.
- **`test_createUser.py`**: Contém testes de integração para verificar a criação de usuários via API.
- **`test_random_hash.py`**: Contém testes unitários para verificar a função `make_random_hash`.

---

### Descrição dos Testes

#### 1. **Exemplo Testes de Integração**

##### Arquivo: `test_createUser.py`
Este arquivo testa o endpoint de criação de usuários, verificando:

- **`test_user_creation_must_return_status_201_and_object_with_user_data`**:  
  Verifica se a criação de um usuário válido retorna status `201` e os dados corretos no objeto de resposta.

- **`test_user_creation_must_return_status_400_and_error_message`**:  
  Verifica se a criação de um usuário com dados inválidos retorna status `400` e uma mensagem de erro apropriada.

---

#### 2. **Exemplo de Testes Unitários**

##### Arquivo: `test_random_hash.py`  
Este arquivo testa a função `make_random_hash`, que gera uma string hash aleatória.

- **`test_make_random_hash_length`**:  
  Verifica se o hash gerado possui exatamente 64 caracteres.

- **`test_make_random_hash_uniqueness`**:  
  Verifica se dois hashes gerados consecutivamente são diferentes, garantindo a unicidade.

---

## Fluxo de Criação e Descarte do Banco de Dados em `conftest.py`

#### 1. **Configuração Inicial:**

No início do `conftest.py`, temos a função `pytest_configure()` que remove o middleware `ObservabilityMiddleware` da configuração antes de executar os testes:

```python
def pytest_configure():
    settings.MIDDLEWARE.remove(
        "todo.middlewares.observabilityMiddleware.ObservabilityMiddleware"
    )
```

Isso garante que o middleware de observabilidade não interfira nos testes.

---

#### 2. **Fixture `client`:**

A fixture `client` cria uma instância do cliente de teste do Django REST Framework (`APIClient`), usada para enviar requisições HTTP nos testes.

```python
@fixture(scope="session")
def client(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        client = APIClient()
        yield client
```

- **`django_db_setup`**: Configura o banco de dados temporário para a sessão de testes.
- **`django_db_blocker.unblock()`**: Permite a execução de operações no banco de dados durante os testes, desbloqueando o acesso temporário.

O banco de dados é criado automaticamente pelo `pytest-django` com base nas configurações do Django (`settings.DATABASES`) e é descartado automaticamente no final da execução dos testes.

---

#### 3. **Fixture `auth_token`:**

Essa fixture realiza uma requisição de login e retorna o token de autenticação, que será usado nos testes para autenticar o cliente.

```python
@fixture(scope="session")
def auth_token(client):
    response = client.post(
        "/auth/login/", data={"username": "admin", "password": "admin"}, format="json"
    )
    yield response.data["access"]
```

- Ela utiliza o cliente `APIClient` para fazer a requisição POST no endpoint `/auth/login/`.
- O token de autenticação é retornado para ser usado nos testes que exigem autenticação.

---

#### 4. **Fixture `auth_client`:**

Essa fixture configura o cliente autenticado, adicionando o token de autenticação no cabeçalho de cada requisição.

```python
@fixture(scope="session")
def auth_client(auth_token, client):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")
    yield client
```

---

#### 5. **Fixture `create_users`:**

Essa fixture utiliza a `UserFactory` para criar um lote de 5 usuários fictícios no banco de dados temporário.

```python
@fixture
def create_users():
    return UserFactory.create_batch(5)
```

---

### Criação e Descarte do Banco de Dados

O banco de dados temporário é gerenciado automaticamente pelo `pytest`, com o seguinte fluxo:

1. **Criação:**  
   - Antes de executar os testes, a fixture cria um banco de dados temporário baseado nas configurações do Django.
   - As migrações são aplicadas automaticamente para configurar o esquema do banco de dados.

2. **Uso nos Testes:**  
   - Durante a execução dos testes, todas as operações de banco de dados (como inserções, atualizações, e exclusões) são realizadas nesse banco de dados temporário.
   - O banco é isolado para garantir que os dados criados em um teste não afetem outros testes.

3. **Descarte:**  
   - Após a execução de todos os testes, o banco de dados temporário é automaticamente descartado.
   - Isso garante que nenhum dado de teste seja persistido após a execução.

---

#### Vantagens do Banco de Dados Temporário

- **Isolamento:** Cada execução de teste é completamente isolada, evitando efeitos colaterais entre os testes.
- **Automação:** O `pytest-django` gerencia automaticamente a criação e o descarte do banco de dados, reduzindo a necessidade de configuração manual.
- **Desempenho:** O uso de um banco de dados temporário minimiza o risco de erros relacionados a dados persistentes entre diferentes execuções de teste.

---

### Como Executar os Testes

#### 1. Configurar ambiente

**Acessar pasta correta**

```
    cd main_app
```

**Criar ambiente virtual**

```
    python -m venv ./venv
```

**Ativar ambiente virtual**

```
   ./venv/Scripts/activate
```

**Baixar dependências**

```
    pip install -r requirements.txt
```

#### 2. Executar os Testes

```
    pytest
```

#### 3. Resultados

![Resultado dos testes](./images/image.png)

---


## Informações adicionais

### Confirmação de email

Ao fazer uma requisição para criar conta, será enviado ao RabbitMQ uma mensagem com o token de liberação da conta gerado e o email para envio. A aplicação de envio de email realiza a formatação e o envio, baseado na leitura das mensagens no RabbitMQ, então somente acessando o link no email será possível ativar a conta e usar as funcionalidades.

### DER (Diagrama Entidade Relacionamento)

Parte do processo de desenvolvimento se deu ao planejamento, diagramação e prototipação. E o diagrama abaixo representa o banco de dados utilizado:

![Imagem do diagrama entidade relacionamento](./images/DER.png)