from envs.lettuce import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lettuce_test.sqlite3',
        'TEST_NAME': ':memory:',
    }
}
