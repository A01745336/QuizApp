# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689

# This is the settings file for a Django web application. It contains various configurations such as
# database settings, installed apps, middleware, and static file directories. The `import os` and
# `from pathlib import Path` lines are used to set the `BASE_DIR` variable to the parent directory of
# the current file, which is commonly used in Django projects to reference other files and
# directories. The `SECRET_KEY` is a unique string used for cryptographic signing and should be kept
# secret. The `ALLOWED_HOSTS` list contains the domain names or IP addresses that the application is
# allowed to run on. The `INSTALLED_APPS` list contains the names of all the Django apps that are
# installed in the project. The `MIDDLEWARE` list contains the middleware classes that are used in the
# project. The `TEMPLATES` list contains the configuration for the Django template engine. The
# `DATABASES` dictionary contains the settings for the database that the application will use. The
# `STATICFILES_DIRS` list contains the directories where static files (such as CSS and JavaScript
# files) are stored.
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '^adwke-#3oll)1@5wu-%p=d4%i_6vuo+hg@8(kgvoyubpn(*jc'

DEBUG = True

ALLOWED_HOSTS = [
    '44.211.170.92',
    'ec2-54-162-66-153.compute-1.amazonaws.com',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Quiz',
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

ROOT_URLCONF = 'Deployment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
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

WSGI_APPLICATION = 'Deployment.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quizapp4',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'database-2.c0fd1vp0jts0.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
