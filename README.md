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
    * [Confirmação de email](confirmacao-de-email)

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

## Informações adicionais

### Confirmação de email

Ao fazer uma requisição para criar conta, será enviado ao RabbitMQ uma mensagem com o token de liberação da conta gerado e o email para envio. A aplicação de envio de email realiza a formatação e o envio, baseado na leitura das mensagens no RabbitMQ, então somente acessando o link no email será possível ativar a conta e usar as funcionalidades.