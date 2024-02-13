import time
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def other_sample_task():
    time.sleep(1)
    logger.info("The sample task just ran.")


@shared_task(queue="celery_first")
def task_to_queue_first():
    time.sleep(1)
    logger.info("The task to queue first just ran.")


@shared_task(queue="celery_second")
def task_to_queue_second():
    time.sleep(2)
    logger.info("The task to queue second just ran.")


@shared_task(queue="celery_third")
def task_to_queue_third():
    time.sleep(3)
    logger.info("The task to queue third just ran.")


@shared_task(queue="celery_fourth")
def task_to_queue_fourth():
    time.sleep(4)
    logger.info("The task to queue fourth just ran.")


"""
Task Chaining
from celery import chain, group
from tasks import task_to_queue_first, task_to_queue_second, task_to_queue_third, task_to_queue_fourth
task_chain = chain(task_to_queue_second.s(), task_to_queue_third.s(), task_to_queue_fourth.s())
task_chain = group(task_to_queue_first.s(), task_to_queue_second.s(), task_to_queue_third.s(), task_to_queue_fourth.s())
task_chain.apply_async()
task_to_queue_first.apply_async(priority=1)
task_to_queue_second.apply_async(priority=2)
task_to_queue_third.apply_async(priority=3)
"""
