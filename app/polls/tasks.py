from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)


@shared_task(name="sample_task")
def sample_task():
    logger.info("The sample task just ran.")


@shared_task(name="send_email_report")
def send_email_report():
    call_command("email_report")
