# Django CRUD + File Upload (PostgreSQL)

## Pré-requisitos

Instalar os pacotes necessários: ```pip install -r requirements.txt```

## Uso

- Configurar o banco de dados usando o ```.env``` a partir do ```.env.example```
- Começar o servidor: ```python manage.py runserver```

## Como um CRUD desse pode ser construído?

- Checar comentários principalmente no arquivo ```settings.py```.
- ```python -m venv venv``` para criar um virtual environment.
- ```source venv/bin/activate``` para ativar o virtual environment.
- ```pip install django djangorestframework django-cors-headers psycopg2 python-dotenv```
- ```pip freeze > requirements.txt```
- No diretório onde a pasta venv está: ```django-admin startproject <project_name>```
- No diretório ```<project_name>```:
    - ```python manage.py dbshell``` testa a conexão com o banco de dados (feita em settings.py).
    - ```python3.9 manage.py startapp <app_name>``` cria um App.
    - ```python3.9 manage.py inspectdb > ./<app_name>/models.py``` cria os models de acordo com um banco de dados existente.
        - Pode ser necessário fazer configurações a mais na mão mas o comando faz o essencial.
    - ```python3.9 manage.py makemigrations <app_name>``` cria as migrations a partir dos models.
    - ```python3.9 manage.py migrate <app_name>``` aplica as migrations no banco de dados.
        - Executar esse comando se você está criando um banco de dados do zero e ainda não possui tabelas com dados.
    - ```python3.9 manage.py migrate <app_name> --fake-initial``` também aplica as migrations no banco de dados.
        - Porém, o --fake-initial serve para aplicar as migrations apenas onde é possível. Ele ignora as migrations onde as tabelas já existem. Ou seja, executar esse comando se você não começou um banco de dados do zero, se você está conectando em um banco de dados que já possui dados armazenados.