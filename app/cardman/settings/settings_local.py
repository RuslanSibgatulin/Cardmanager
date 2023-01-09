import os
from pathlib import Path

from split_settings.tools import include

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = os.environ.get("DJANGO_DEBUG", False) == "True"

ALLOWED_HOSTS = ["127.0.0.1"]

ROOT_URLCONF = "cardman.urls"

WSGI_APPLICATION = "cardman.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
STATIC_ROOT = "static"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

include(
    "logger.py",  # LOGGING
    "middleware.py",  # Middleware
    "templates.py",  # Templates
    "auth.py",  # Auth
    "message_tags.py",
    "celery_conf.py",
    "apps.py",
)
