# Python Imports
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']  # Allow all hosts in development

# Use SQLite database in development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
