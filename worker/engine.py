import os
from celery import Celery
from celery.utils.log import get_task_logger
from kombu import Exchange, Queue


logger = get_task_logger(__name__)

celery_worker = Celery(
    name="celery_worker",
    broker_url=os.getenv("CELERY_BROKER_URL"),
    result_backend=os.getenv("CELERY_RESULT_BACKEND"),
    include=["tasks"],
    result_persistent=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    broker_transport_options={
        "max_retries": 1,
        "visibility_timeout": 365 * 24 * 60 * 60,
    },
)

celery_worker.conf.task_queues = (
    Queue(
        "celery_first",
        Exchange("celery_first"),
        routing_key="celery_first",
        queue_arguments={"x-max-priority": 10},
    ),
    Queue(
        "celery_second",
        Exchange("celery_second"),
        routing_key="celery_second",
        queue_arguments={"x-max-priority": 10},
    ),
    Queue(
        "celery_third",
        Exchange("celery_third"),
        routing_key="celery_third",
        queue_arguments={"x-max-priority": 10},
    ),
    Queue(
        "celery_fourth",
        Exchange("celery_fourth"),
        routing_key="celery_fourth",
        queue_arguments={"x-max-priority": 10},
    ),
)

celery_worker.conf.task_routes = {
    "tasks.other_task": {"queue": "celery_first"},
    "tasks.other_sample_task": {"queue": "celery_first"},
    "tasks.task_to_queue_first": {"queue": "celery_first"},
    "tasks.task_to_queue_second": {"queue": "celery_second"},
    "tasks.task_to_queue_third": {"queue": "celery_third"},
    "tasks.task_to_queue_fourth": {"queue": "celery_fourth"},
}

celery_worker.conf.task_ack_late = True
celery_worker.conf.task_reject_on_worker_lost = True
celery_worker.conf.worker_prefetch_multiplier = 1
celery_worker.conf.worker_concurrency = 3
celery_worker.conf.task_default_queue = "celery_first"
celery_worker.conf.task_default_exchange = "celery_first"
celery_worker.conf.task_default_routing_key = "celery_first"


@celery_worker.task()
def other_sample():
    print("The sample task for other celery just ran.")


celery_worker.autodiscover_tasks()
