"""
Django settings for test_project project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9nm(-!mt9n@35*kteohoa4g1e@bqnx6l@o=0m*4s%*u4o0c_0='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary',
    'datetimewidget',
    'home', # a dummy home page for development purposes
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'test_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'test_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# the django default does not allow time with meridian
TIME_INPUT_FORMATS = (
    '%H:%M:%S',
    '%H:%M',
    '%I %p',
    '%I:%M %p',
    '%I:%M%p',
    '%H:%M:%S.%f',
)

DIARY_MULTI_DAY_NUMBER = 5

#DIARY_SHOW_MERIDIAN = True
#DIARY_FIRST_DAY_OF_WEEK = 6

DIARY_MIN_TIME = datetime.time(hour=6)
DIARY_MAX_TIME = datetime.time(hour=20)
#DIARY_TIME_INC = datetime.timedelta(minutes=15)

week_opening_time = datetime.time(hour=9)
sunday_opening_time = datetime.time(hour=10, minute=30)
DIARY_OPENING_TIMES = {n: week_opening_time for n in range(0, 6)}
DIARY_OPENING_TIMES[6] = sunday_opening_time

week_closing_time = datetime.time(hour=18)
sunday_closing_time = datetime.time(hour=16, minute=30)
DIARY_CLOSING_TIMES = {n: week_closing_time for n in range(0, 6)}
DIARY_CLOSING_TIMES[6] = sunday_closing_time

DIARY_MIN_BOOKING = 1

DIARY_CONTACT_PHONE = '01234567890'

# User customisation
# NOTE: use of InheritanceQuerySet in the backend dispenses with the need for 
# any other setting. (django-model-utils)
# http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance/
AUTHENTICATION_BACKENDS = (
    'diary.backends.CustomUserModelBackend',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


# test email server setup
if DEBUG:
    ADMINS = (
        ('Mr Big', 'admin@example.com'),
        ('Mrs Big', 'admin2@example.com'),
    )
    SERVER_EMAIL = 'root@example.com'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'testing@example.com'

