# ContactsApp

Mini aplicação para gestão de contactos

## Setup

Setup inicial.

```sh
flask db init
```

Rodar o comando abaixo toda vez que a estrutura do banco de dados mudar.

```sh
flask db migrate
flask db upgrade
```

## Executar com Docker

```sh
docker run -p 5000:5000 --name cesae-contacts-app cesae-contacts-app:2.1.1
```

### Rodar as migrations

```sh
docker exec -it [NOME_DO_CONTAINER] sh
flask db upgrade
```
