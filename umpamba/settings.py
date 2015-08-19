"""
Django settings for umpamba project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&95+7!-gbp-p9t$pw8x3$j#o1k@k&6n6sv2h-_1ve#zsz_l$fe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newscoder'
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

ROOT_URLCONF = 'umpamba.urls'

WSGI_APPLICATION = 'umpamba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

## LOGGING = {
##     'version': 1,
##     'disable_existing_loggers': False,
##     'filters': {
##         'require_debug_false': {
##             '()': 'django.utils.log.RequireDebugFalse'
##         }
##     },
##     'handlers': {
##         ## 'mail_admins': {
##         ##     'level': 'ERROR',
##         ##     'filters': ['require_debug_false'],
##         ##     'class': 'django.utils.log.AdminEmailHandler'
##         ## }
##         'applogfile': {
##             'level':'DEBUG',
##             'class':'logging.handlers.RotatingFileHandler',
## #            'filename': os.path.join(DJANGO_ROOT, 'APPNAME.log'),
##             'filename': '/tmp/django.log',
##             'maxBytes': 1024*1024*15, # 15MB
##             'backupCount': 10,
##         },
##     },
##     'loggers': {
##         'django.request': {
##             'handlers': ['applogfile'],
##             'level': 'ERROR',
##             'propagate': True,
##         },
##     }
## }
