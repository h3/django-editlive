from envs.dev import *

# Dev specific stuff
SITE_ID = 2

SOUTH_TESTS_MIGRATE = False

# Use mysql, for actually relevant results
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'salad_test_project.sqlite3',
        'USER': 'root',
        'PASSWORD': '',
    }
}

LETTUCE_AVOID_APPS = (
    "analytical",
    "annoying",
    # "archetype", # uncomment this once your app is up and running.
    "compressor",
    "django_extensions",
    "gunicorn",
    "south",
    "django.contrib.staticfiles",
)

LETTUCE_SERVER_PORT = 9000
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
