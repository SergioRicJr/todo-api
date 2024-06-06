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
    * [Aplicação para envio de email](#aplicacao-para-envio-de-email)

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