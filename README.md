# Guia de Configuração da Aplicação Django com Docker

Este guia explica como usar o Docker e o Docker Compose para configurar uma aplicação Django que utiliza um banco de dados PostgreSQL. **Certifique-se de que o Docker Desktop esteja ativo em seu PC.**

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado.
- [Docker Compose](https://docs.docker.com/compose/install/) instalado.

## Estrutura do Projeto

Antes de começar, certifique-se de que sua estrutura de diretório esteja organizada da seguinte forma:

```
/seu-projeto
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── poetry.lock
└── manage.py
```

## Dockerfile

O `Dockerfile` abaixo usa a imagem oficial do Python como base e instala as dependências necessárias para a sua aplicação.

```dockerfile
# Use a imagem oficial do Python como base
FROM python:3.12-slim as python-base

# Defina variáveis de ambiente para o Python e Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.5.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adicione Poetry e venv ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instale o Git e dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    git \
    && apt-get clean

# Instale o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Instale dependências adicionais para PostgreSQL
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gcc \
    && apt-get clean

# Defina o diretório de trabalho e copie arquivos de requisitos
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Instale as dependências do Python usando o Poetry
RUN poetry install --no-interaction --no-dev  # Use --no-dev para instalar apenas dependências principais

# Copie o requirements.txt e instale as dependências do pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copie o código fonte da aplicação
WORKDIR /app
COPY . /app/

# Exponha a porta da aplicação
EXPOSE 8000

# Execute a aplicação Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## docker-compose.yml

O `docker-compose.yml` abaixo configura os serviços para a aplicação Django e o banco de dados PostgreSQL.

```yaml
version: "3.8"

services:
  db:
    image: postgres:13.0-alpine
    ports:
      - 5432:5432
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      POSTGRES_USER: bookstore_dev
      POSTGRES_PASSWORD: bookstore_dev
      POSTGRES_DB: bookstore_dev_db

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app # Mapeie o diretório onde manage.py está localizado
    ports:
      - 8000:8000
    env_file:
      - ./env.dev
    depends_on:
      - db

volumes:
  postgres_data:
```

## requirements.txt

Certifique-se de que seu arquivo `requirements.txt` esteja configurado corretamente. Aqui está um exemplo baseado nas dependências que você forneceu:

```plaintext
asgiref==3.8.1
-e git+https://github.com/AugustoCedric/bookstore.git@ce9055338ca4bd07e35fd9e6e797a77d0760e2bd#egg=bookstore
colorama==0.4.6
Django==5.1.2
django-debug-toolbar==4.4.6
django-extensions==3.2.3
djangorestframework==3.15.2
factory_boy==3.3.1
Faker==30.6.0
gitdb==4.0.11
GitPython==3.1.43
iniconfig==2.0.0
packaging==24.1
pluggy==1.5.0
psycopg2-binary==2.9.10
pytest==8.3.3
python-dateutil==2.9.0.post0
six==1.16.0
smmap==5.0.1
sqlparse==0.5.1
typing_extensions==4.12.2
tzdata==2024.2
whitenoise==6.7.0
```

## Instruções para Executar

### Limpar Contêineres e Imagens Existentes

Antes de iniciar sua aplicação, você pode querer limpar os contêineres e imagens antigos. Execute os seguintes comandos:

```bash
# Remove todos os contêineres
docker rm -vf $(docker ps -aq)

# Remove todas as imagens
docker rmi -f $(docker images -aq)

# Remove volumes órfãos
docker volume rm $(docker volume ls -qf dangling=true)

# Limpa volumes
docker volume prune
```

### Iniciar a Aplicação

1. **Abra um terminal** e navegue até o diretório do seu projeto.

2. **Construa e inicie os contêineres** com o seguinte comando:

   ```bash
   docker-compose up -d --build
   ```

3. **Aplique as migrações** para o banco de dados:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Para executar os testes** da sua aplicação, utilize o seguinte comando:

   ```bash
   docker-compose exec web python manage.py test
   ```

5. **Acesse a aplicação** em um navegador da web em `http://localhost:8000`.

6. **Para parar os contêineres**, pressione `CTRL + C` no terminal ou execute:

   ```bash
   docker-compose down
   ```

## Conclusão

Você agora deve ter uma aplicação Django rodando com um banco de dados PostgreSQL usando Docker e Docker Compose. Se você encontrar algum problema, verifique os logs no terminal para obter mensagens de erro e depurar conforme necessário.

```

```
