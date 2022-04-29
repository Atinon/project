from os import getenv
from pathlib import Path

import cloudinary

from exam_project.utils.utils import is_production

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = getenv('DEBUG', 'False') == 'True'
print(f'Debug: {DEBUG}')

APP_ENVIRONMENT = getenv('APP_ENVIRONMENT', 'Development')
print(APP_ENVIRONMENT)

SECRET_KEY = getenv('SECRET_KEY', 'backupsecretkey')

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', '').split(' ')

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ()

PROJECT_APPS = (
    'exam_project.accounts',
    'exam_project.main',
    'exam_project.comments',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'exam_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'exam_project.wsgi.application'

DEFAULT_DATABASE_CONFIG = None

if is_production():
    DEFAULT_DATABASE_CONFIG = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd7mjd36p00b6id',
        'USER': 'mgvkzzrvddincs',
        'PASSWORD': 'a37716442a2b61c0a66757449d6a3660ea4483bac7338ebacff8ba059505829b',
        'HOST': 'ec2-34-242-8-97.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
else:
    DEFAULT_DATABASE_CONFIG = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'exam_project_db',
        'USER': 'postgres',
        'PASSWORD': '1123QwER',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }

DATABASES = {
    'default': DEFAULT_DATABASE_CONFIG,
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

if is_production():
    AUTH_PASSWORD_VALIDATORS.extend([
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
    ])

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

if DEBUG:
    STATICFILES_DIRS = (
        BASE_DIR / 'staticfiles',
        BASE_DIR / 'staticfiles/bootstrap',
    )
else:
    STATIC_ROOT = BASE_DIR / 'staticfiles/'
    STATICFILES_DIRS = (
        # BASE_DIR / 'staticfiles',
        BASE_DIR / 'staticfiles/bootstrap',
    )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATIC_URL = '/static/'

# MEDIA_ROOT = BASE_DIR / 'staticfiles/mediafiles/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.ProjectUser'

cloudinary.config(
    cloud_name=getenv('CLOUDINARY_CLOUD_NAME', None),
    api_key=getenv('CLOUDINARY_API_KEY', None),
    api_secret=getenv('CLOUDINARY_API_SECRET', None),
)