import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

celery_app = Celery(
    "core",
    broker_url=os.getenv("CELERY_BROKER_URL"),
    result_backend=os.getenv("CELERY_RESULT_BACKEND"),
    result_persistent=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    broker_transport_options={
        "max_retries": 1,
        "visibility_timeout": 365 * 24 * 60 * 60,
    },
)

celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
