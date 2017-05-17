"""
Django settings for controlc project.

Generated by 'django-admin startproject' using Django 1.10a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
from django.core.urlresolvers import reverse_lazy
#PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3_idz0%w(lwlxqmp&2!wfjd*%q#v2fndfxfwf%tg!%o)v&tpj3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # APPS O COMPONENTES DE TERCEROS
    'django_tables2',
    'widget_tweaks',
    'crispy_forms',
    # 'simple_forms.apps.core',
    # Mis aplicaciones
    'controlc',
    'configuracion',
    'administracion',
    'establecimiento'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'controlc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'plantillas/'),
            os.path.join(BASE_DIR, 'configuracion/vistas/'),
            os.path.join(BASE_DIR, 'establecimiento/vistas/')
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Componentes de terceros
                'django.template.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'controlc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbcontrolc',
        'USER': 'dbmicolegiouser',
        'PASSWORD': 'adm1nm1colegio123*',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

DEFAULT_CHARSET = 'utf-8'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
LOGIN_REDIRECT_URL = '/'
# LOGIN_URL = '/plantillas/cuentasUsuario/'
# LOGIN_REDIRECT_URL = '/plantillas/cuentasUsuario/'
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.core.context_processors.request'
# )

#LOGIN_URL = #reverse_lazy('login')
#LOGIN_REDIRECT_URL = reverse_lazy('menu')
LOGOUT_URL = reverse_lazy('logout')
LOGIN_URL = reverse_lazy('controlc:login')

CRISPY_TEMPLATE_PACK = 'bootstrap3'
#AUTH_USER_MODEL = 'configuracion.User'
