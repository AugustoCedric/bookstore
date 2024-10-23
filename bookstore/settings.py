import os
from pathlib import Path

# Caminhos dentro do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de segurança
SECRET_KEY = "django-insecure-f*k@=53bc5!shef1-6w+m$-g)kspbaljz%8k4(j7iuc-u2_dyd"
DEBUG = True

<<<<<<< HEAD
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-#7ajm6gp(#n8_j_yvx$%qd+7$b)+1+ooqgwvr8x+vq(6@al6^n",
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"


ALLOWED_HOSTS = ["localhost", "127.0.0.1", "cedric.pythonanywhere.com"]


# Application definition
=======
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "ebac-bookstore-api1-9d9b47b419f3.herokuapp.com",
    "maiconveiga.pythonanywhere.com",
]
>>>>>>> 5a21c122a215ffb873d38452e1041eb422095765

# Definição das aplicações instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "order",
    "product",
    "rest_framework",
    "rest_framework.authtoken",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

if DEBUG:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

# URLs e templates
ROOT_URLCONF = "bookstore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
<<<<<<< HEAD
        "DIRS": [os.path.join(BASE_DIR, "bookstore", "templates")],
=======
        "DIRS": [BASE_DIR / "bookstore" / "templates"],
>>>>>>> 5a21c122a215ffb873d38452e1041eb422095765
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bookstore.wsgi.application"

# Configurações do banco de dados
DATABASES = {
    "default": {
<<<<<<< HEAD
        # "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        # "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "bookstore_dev_db"),
=======
>>>>>>> 5a21c122a215ffb873d38452e1041eb422095765
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "bookstore_dev"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "bookstore_dev"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internacionalização
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "staticfiles"

<<<<<<< HEAD
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # Adjust as needed for your project

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # Adjust as needed for your project


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


=======
# Configurações do Django REST Framework
>>>>>>> 5a21c122a215ffb873d38452e1041eb422095765
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

# Configurações do Debug Toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

<<<<<<< HEAD

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = BASE_DIR / "staticfiles"
=======
# Campo de chave primária padrão
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
>>>>>>> 5a21c122a215ffb873d38452e1041eb422095765
