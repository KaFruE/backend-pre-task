from ._base import *
import os

DEBUG = False

ALLOWED_HOSTS += []

WSGI_APPLICATION = 'conf.wsgi.prod.application'

INSTALLED_APPS += [
]

MIDDLEWARE += [
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# # 작업 주의사항 : sqlite가 아닌 MySQL 설정으로 변경해 주세요
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prod',
        'USER': 'root',
        'PASSWORD': '6442',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
