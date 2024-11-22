# Local Imports
from .base import *

# Python Imports
import os


ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["maazsabahuddin.com"])

# Database configuration for production
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': env("DJANGO_DB_NAME"),
    #     'USER': env("DJANGO_DB_USER"),
    #     'PASSWORD': env("DJANGO_DB_PASSWORD"),
    #     'HOST': env("DJANGO_DB_HOST", default="localhost"),
    #     'PORT': env("DJANGO_DB_PORT", default="5432"),
    # }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email backend configuration for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env("DJANGO_EMAIL_HOST")
EMAIL_PORT = env.int("DJANGO_EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("DJANGO_EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")
