"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from pathlib import Path

from django.core.asgi import get_asgi_application
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = os.path.join(BASE_DIR, ".env")
env = environ.Env(
    # Set casting / default false
    DEBUG=(bool, False)
)
environ.Env.read_env(env_file=os.path.join(ENV_PATH))

if env("DEBUG"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_asgi_application()
