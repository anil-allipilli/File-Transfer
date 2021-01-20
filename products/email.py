from django.core.mail import EmailMessage
from django.conf import settings


def send_users_mail(product_name, product_creater, users_list):

    email_subject = "A product was shared with you"
    email_body = (
        "user {product_owner} has shared a product named {product_name}".format(
            product_owner=product_creater, product_name=product_name
        )
    )
    email = EmailMessage(
        email_subject, email_body, settings.DEFAULT_FROM_EMAIL, users_list
    )
    return email.send(fail_silently=False)
