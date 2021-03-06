from celery.decorators import task
from celery.utils.log import get_task_logger

from .email import send_staff_email

logger = get_task_logger(__name__)


@task(name="send_staff_email_task")
def send_staff_email_task(name, company, email):
    logger.info("Sent email")
    return send_staff_email(name, company, email)