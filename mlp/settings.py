"""
Django settings for mlp project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

from decouple import config

# Importing settings for subsystem
from .settings_tracker import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    config("DJANGO_ALLOWED_HOSTS", default="localhost"),
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = ["https://ml4dqm-playground.web.cern.ch"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrap3",
    "django_tables2",
    "django_extensions",
    "widget_tweaks",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "home.apps.HomeConfig",
    "tables.apps.TablesConfig",
    "listdatasets.apps.ListdatasetsConfig",
    "dataset_tables.apps.DatasetTablesConfig",
    "histograms",
    "histogram_file_manager",
    "challenge",
    "data_taking_objects",
    "data_taking_certification",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mlp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

# WSGI_APPLICATION = "mlp.wsgi.application"
ASGI_APPLICATION = "mlp.asgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DJANGO_DATABASE_ENGINE", default=""),
        "NAME": config("DJANGO_DATABASE_NAME", default=""),
        "USER": config("DJANGO_DATABASE_USER", default=""),
        "PASSWORD": config("DJANGO_DATABASE_PASSWORD", default=""),
        "HOST": config("DJANGO_DATABASE_HOST", default=""),
        "PORT": config("DJANGO_DATABASE_PORT", default=""),
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG" if DEBUG else "WARNING",
    },
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} - {module} - {message}",
            "style": "{",
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },

        #     'daphne': {
        #         'handlers': [
        #             'console',
        #         ],
        #         'level': 'DEBUG'
        #     },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "home/static"),
    # os.path.join(BASE_DIR, "run_histos/static"),
    # os.path.join(BASE_DIR, "lumisection_histos1D/static"),
    os.path.join(BASE_DIR, "common/static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Notebook arguments
NOTEBOOK_ARGUMENTS = [
    # exposes IP and port
    "--ip=127.0.0.1",
    "--port=8000",
    # disables the browser
    "--no-browser",
]

# Root directory where DQM files are stored, no default for safety
DIR_PATH_EOS_CMSML4DC = config("DIR_PATH_EOS_CMSML4DC")

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",  # will require authentication
        # 'rest_framework.permissions.AllowAny',  # Allow any user, no need for authentication
    ],
    "DEFAULT_FILTER_BACKENDS":
    ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS":
    "mlp.pagination.MLPlaygroundAPIPagination",
    "PAGE_SIZE":
    50,
}
LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/"
