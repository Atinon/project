from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1v7j1%p8__+4(q%pxc%_l*b0(o%t#y8jxnewfz1*764_pstc!6'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = getenv('DEBUG', 'False') == True
DEBUG = True

ALLOWED_HOSTS = [
    'wndr-project.herokuapp.com',
    'localhost',
    '127.0.0.1',
]

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
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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

if DEBUG:
    default = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'exam_project_db',
        'USER': 'postgres',
        'PASSWORD': '1123QwER',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
else:
    default = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbldk269bj8co6',
        'USER': 'qxlvvjezyzqcmo',
        'PASSWORD': '393cbe6834bdcda9a023fdc58f640c0c2e8d4ed96390c2dd27e5963c2120de5f',
        'HOST': 'ec2-63-32-248-14.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }

DATABASES = {
    'default': default,
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (
    # BASE_DIR / 'staticfiles',
    BASE_DIR / 'staticfiles/mediafiles',
)
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / 'staticfiles/mediafiles/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.ProjectUser'
