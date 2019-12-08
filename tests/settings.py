import os
import sys

BASE_DIR = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.sqlite3',
    }
}

INSTALLED_APPS = [
    'tests',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
SILENCED_SYSTEM_CHECKS = (
    'admin.E130',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'tests/templates')
        ],
        'OPTIONS': {
            'debug': True,
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ),
            'context_processors': (
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
            )
        }
    },
]

# Setting for pytest-django
# https://pytest-django.readthedocs.io/en/latest/faq.html
TEST_RUNNER = 'run_test.PytestTestRunner'
DJANGO_SETTINGS_MODULE = 'tests.settings'

DOMAIN = 'http://localhost'
ROOT_URLCONF = 'tests.urls'
SECRET_KEY = "dummy"
