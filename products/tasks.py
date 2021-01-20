from celery.decorators import task
from celery.utils.log import get_task_logger
from products.email import send_users_mail

logger = get_task_logger(__name__)


@task(name="send_users_product_creation_notification")
def send_product_email_to_users(product_name, product_creater, users_list):
    logger.info("Product email sent")
    return send_users_mail(product_name, product_creater, users_list)