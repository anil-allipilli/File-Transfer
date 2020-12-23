from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_staff_email(name, company, email):

    email_subject = "A new user registered"
    email_body = "{name} with company {company}  with email address {email}.".format(
        name=name, company=company, email=email
    )

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [
            settings.DEFAULT_FROM_EMAIL,
        ],
    )
    return email.send(fail_silently=False)
