from dev import *

VIRTUALENV_NAME = "editlive_test_env"

DEBUG = True
TEMPLATE_DEBUG = True
DAJAXICE_DEBUG = True

SOUTH_TESTS_MIGRATE = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'CACHE+' + SECRET_KEY
    }
}
