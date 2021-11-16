"""
Django settings for django_crud project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
#  ---------------------------------------------------------------------------

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Tornou possivel o upload de arquivos

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict = True).parent.parent
MEDIA_URL = '/Files/'
MEDIA_ROOT = os.path.join(BASE_DIR,'Files')

#  ---------------------------------------------------------------------------

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^im#@u_n@tm4@3sp#*b%@6b$k(js5q@(11^hc&eeij1^6msh=3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#  ---------------------------------------------------------------------------

# Application definition

# Os ultimos 3 elementos do array abaixo foram adicionados manualmente
# O ultimo elemento seria o diretorio '<app_name>.apps.<class_name>', em que <class_name> eh o nome da classe que aparece no arquivo apps.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'App.apps.AppConfig'
]

# A linha abaixo foi adicionada manualmente. Ela eh recomendada apenas no desenvolvimento. Quando colocar o projeto em producao tem que buscar outra solucao.

CORS_ORIGIN_ALLOW_ALL = True

# O primeiro elemento do array abaixo foi adicionado manualmente

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#  ---------------------------------------------------------------------------

ROOT_URLCONF = 'django_crud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_crud.wsgi.application'

#  ---------------------------------------------------------------------------

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

from dotenv import load_dotenv

load_dotenv()

# OPTIONS serve para dar o comando inspectdb num schema especifico, no caso eh o sihab
# Se as tabelas estiverem no schema default (public), pode remover a linha do OPTIONS
# No caso de ainda não existirem tabelas (criar elas a partir das migrations), pode remover a linha do OPTIONS tambem

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
        'OPTIONS': {
            'options': '-c search_path='+os.getenv('DATABASE_SEARCH_PATH')
        }
    }
}

#  ---------------------------------------------------------------------------

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
