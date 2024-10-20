# Use the official Python image as base
FROM python:3.12-slim as python-base

# Set environment variables for Python and Poetry
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

# Add Poetry and venv to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install dependencies for Python and PostgreSQL
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    git \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  # Clean up APT cache to reduce image size

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set working directory and copy requirements files
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Install Python dependencies using Poetry
RUN poetry install --no-interaction

# Copy the application code
WORKDIR /app
COPY . /app/

# Expose the application port
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
