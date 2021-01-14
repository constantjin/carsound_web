import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = os.path.join(BASE_DIR, ".env")

# Django-environ
env = environ.Env(
    # Set casting / default false
    DEBUG=(bool, False),
)
environ.Env.read_env(env_file=ENV_PATH)

# Set Site Domain
DOMAIN = env("DOMAIN")

# SECURITY
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # Maintenace mode
    "maintenance_mode",
    # Project apps
    "subjects.apps.SubjectsConfig",
    "sounds.apps.SoundsConfig",
    "ratings.apps.RatingsConfig",
    # 3rd Party apps
    "rest_framework",
    "corsheaders",
    "manifest_loader",
    # Django base apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    # 3rd Party middlewares
    "corsheaders.middleware.CorsMiddleware",
    # Django base middlewares
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Django maintenance mode
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "maintenance_mode.context_processors.maintenance_mode",
            ],
            "libraries": {
                "load_manifest": "templatetags.load_manifest",
            },
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
FRONTEND_DIST_PATH = os.path.join(BASE_DIR, "experiment", "dist")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    FRONTEND_DIST_PATH,
)

# Sounds files
SOUNDS_URL = "static/stims/"
SOUNDS_ROOT = os.path.join(BASE_DIR, SOUNDS_URL)
BASE_SOUND_URL = DOMAIN + SOUNDS_URL + "base/" + "carsound.wav"

# Maintenance mode
# if True admin site will not be affected by the maintenance-mode page
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True
MAINTENANCE_MODE_TEMPLATE = "503.html"
MAINTENANCE_MODE_IGNORE_URLS = (r"^/static/", r"^/maintenance/")
MAINTENANCE_MODE_STATE_FILE_PATH = os.path.join(BASE_DIR, "maintenance_mode_state.txt")
