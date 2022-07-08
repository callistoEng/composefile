
from pathlib import Path
import os
# import environ

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'bjt2h8#v&wfgtoe1_btwkes4$^veu&g__2!=groncstfd$yqs-'

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
    'django.contrib.gis',
    'geolocapp',

    'rest_framework',
    'rest_framework_gis',
    'leaflet',
    # 'channels'
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

ROOT_URLCONF = 'coreapp.urls'

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

WSGI_APPLICATION = 'coreapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'NAME': 'postgres',
        # 'USER': 'postgres',
        # 'PASSWORD': 'postgres',
        # 'HOST': 'db',
        # 'PORT':5432,
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'location',
        'USER': 'admin',
        'PASSWORD': 'ad123451',
        'HOST': 'db',
        'PORT':5432
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'django-db',
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': 'db',
    #     'PORT':'3306'
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'  

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_DIR = os.path.join(BASE_DIR, 'build/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/Images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/Images')
STATIC_URL = '/static/'


##leaflet conf##
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-1.94, 29.87),
    'DEFAULT_ZOOM': 8,
    'MAX_ZOOM': 20,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'API-Imperfect Schools Map'
}