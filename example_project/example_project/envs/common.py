from os.path import abspath, join, dirname
from sys import path
from util import environment_settings
globals().update(environment_settings.env_settings())


PROJECT_ROOT = abspath(join(dirname(__file__), "../"))
EDITLIVE_ROOT = abspath(join(PROJECT_ROOT, "../../"))
TEST_APP_ROOT = abspath(join(PROJECT_ROOT, "../test_app/"))

path.insert(0, PROJECT_ROOT)
path.insert(0, EDITLIVE_ROOT)
path.insert(0, TEST_APP_ROOT)

DEV = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'testdb.sqlite3',            # Or path to database file if using sqlite3.
        'USER': '',                       # Not used with sqlite3.
        'PASSWORD': '',                   # Not used with sqlite3.
        'HOST': '',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                       # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'America/Montreal'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
USE_TZ = False

DATE_FORMAT = 'Y-m-d'
DATE_INPUT_FORMATS = ('%Y-%m-%d',)
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATETIME_INPUT_FORMATS = ('%Y-%m-%d %H:%i:%s',)

MEDIA_ROOT = join(PROJECT_ROOT, "media")
MEDIA_URL = '/media/'

STATIC_ROOT = join(PROJECT_ROOT, "static")
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
   #'compressor.finders.CompressorFinder',
)

SECRET_KEY = 'tmw!okt31h*bc$71u--sp^=)d$0ylz&^&&8g!v(eor(tze9j8#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
   #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',    
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'example_project.urls'

#WSGI_APPLICATION = 'editlive_demo.wsgi.application'

TEMPLATE_DIRS = (
    abspath(join(PROJECT_ROOT, "templates"),)
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.markup',
   #'django.contrib.admin',
   #"compressor",
    "lettuce.django",
    'dajaxice',
    "editlive",
    "test_app",
)

STATICFILES_EXCLUDED_APPS = []
COMPRESS_ROOT = STATIC_ROOT

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# See http://docs.djangoproject.com/en/dev/topics/logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
           #'handlers': ['mail_admins'],
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'dajaxice': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'CACHE+' + SECRET_KEY
    }
}
