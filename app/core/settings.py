import os
from pathlib import Path
from celery.schedules import crontab


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-mo5!kunim1rh9f7!d!ltiny$wyf4=0#k-a+ype)#94xi)w@vwc",
)
DEBUG = bool(os.getenv("DEBUG", True))
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(" ")
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     # 'google.com',
#     # 'hostname.example.com',
#     '127.0.0.1:8002',
# )

CORS_ALLOW_METHODS = [
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
    "DELETE",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "Cache-Control",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
    "django.contrib.messages",
    "polls.apps.PollsConfig",
    # "polls.urls",
    # "polls.tasks",
    "corsheaders",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = os.getenv("DJANGO_SETTINGS_URLS", "core.urls")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = os.getenv("DJANGO_WSGI_MODULE", "core.wsgi.application")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres_user",
        "PASSWORD": "mypassword",
        "HOST": "postgres_django",
        "PORT": 5432,
    }
}

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

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.getenv("DATABASE_URL", "db+sqlite:///celery.sqlite")
CELERY_CACHE_BACKEND = "db+sqlite:///celery.sqlite"

CELERY_BEAT_SCHEDULE = {
    "sample_task": {
        "task": "celery-worker.tasks.sample_task",
        "schedule": crontab(minute="*/1"),
    },
    "send_email_report": {
        "task": "celery-worker.tasks.send_email_report",
        "schedule": crontab(hour="*/1"),
    },
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATIC_ROOT = Path("/").joinpath(BASE_DIR, "static/")
