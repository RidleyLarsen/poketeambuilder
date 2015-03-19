"""
Django settings for PokeTeamBuilder.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

DEFAULT_CONTACT_EMAIL = "Ridley Larsen <ridley@" + "velocitywebworks.com>"
DEFAULT_FROM_EMAIL = "Ridley Larsen <ridley@" + "velocitywebworks.com>"

# Misc. Project Settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DIRNAME = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', "static")
STATIC_URL = '/static/'

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
TIME_ZONE = "America/Denver"

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'pokemon',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
)

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, '..', 'templates'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Database Settings
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# See production and development modules for DATABASES.

DATABASE_NAME = "pokeapi"
DATABASE_PASSWORD = "TuTKaAUjuSqJvtNJ"
DATABASE_USER = "pokeapi"
DATABASES = {}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
