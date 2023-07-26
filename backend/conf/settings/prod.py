from ._base import *
import os

DEBUG = False

ALLOWED_HOSTS += []

WSGI_APPLICATION = 'config.wsgi.prod.application'

INSTALLED_APPS += [
]

MIDDLEWARE += [
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# # 작업 주의사항 : sqlite가 아닌 MySQL 설정으로 변경해 주세요
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
