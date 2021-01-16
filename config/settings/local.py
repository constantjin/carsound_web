from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DEV CORS
CORS_ALLOW_ALL_ORIGINS = True
INSTALLED_APPS.remove("django.contrib.staticfiles")

ALLOWED_HOSTS = ["*"]
