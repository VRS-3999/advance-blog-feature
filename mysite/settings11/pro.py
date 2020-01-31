from .base import *

DEBUG = False

ADMINS = (
    ('vivek raj Singh', 'vivekrajs3999@gmail.com'),
    )

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'DRAGONBALL',
        'Port': '5432',
        }
    }
