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

# Adicione esta linha para instalar o Git
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    git \
    && apt-get clean

# Instale o Poetry usando o novo método de instalação
RUN curl -sSL https://install.python-poetry.org | python3 -

# Instale dependências adicionais para PostgreSQL
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gcc \
    && apt-get clean

# Defina o diretório de trabalho e copie os arquivos de requisitos
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
