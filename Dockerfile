# Base python image
FROM python:3.12.1-slim as python-base

# Set environment variables for Python and Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Add Poetry and venv to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        git \
        libpq-dev gcc

# Install Poetry
RUN pip install poetry

# Set working directory for project setup
WORKDIR $PYSETUP_PATH

# Copy the project dependency files
COPY poetry.lock pyproject.toml ./

# Install dependencies, replacing deprecated '--no-dev' with '--only main'
RUN poetry install --only main

# Set working directory for the application
WORKDIR /app

# Copy the rest of the application code
COPY . /app/

# Expose the port for the app
EXPOSE 8000

# Set the default command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
