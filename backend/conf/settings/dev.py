from ._base import *
import os

DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

ALLOWED_HOSTS += []

WSGI_APPLICATION = 'conf.wsgi.dev.application'

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# # 작업 주의사항 : sqlite가 아닌 MySQL 설정으로 변경해 주세요
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev',
        'USER': 'root',
        'PASSWORD': '6442',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
