from .base import *

DEBUG = True

MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
]

INSTALLED_APPS += ["drf_yasg", "silk.apps.SilkAppConfig"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "my-library_db",
        "PORT": "5432",
    }
}
