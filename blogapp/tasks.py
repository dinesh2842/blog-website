from celery import shared_task
from django.core.mail import send_mail
from .models import Subscribe
from blog_website import settings
# @shared_task(bind=True)
# def fun(self):
#     print('you are in Fun function')
#     return 'done'


@shared_task
def send_newsletter_email():
    subscribers = Subscribe.objects.all()
    for sub in subscribers:
        send_mail(
            subject='Latest Blog Posts from Tech Blog!',
            message='Check out our latest blogs now at techblogs.com',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.email],
            fail_silently=True,
        )
    return 'Newsletter sent'

@shared_task
def send_contact_email_to_team(name, email, project, message):
    subject = 'Got a Message from Contact Form'
    body = (
        f"Hi Team,\n\nWe have received a request from user. Please find the below information:\n"
        f"Name: {name}\nEmail: {email}\nProject: {project}\nMessage: {message}\n\nBest regards,\nDevtech"
    )
    send_mail(subject, body, settings.EMAIL_HOST_USER, ['contactus@devtechnician.com'], fail_silently=False)

@shared_task
def send_acknowledgement_email(name, email):
    subject = 'Thanks for Contacting Us'
    body = (
        f"Hi {name},\nThank you for submitting a request. Our team will get in touch with you shortly.\n\nBest regards,\nDevtech"
    )
    send_mail(subject, body, settings.EMAIL_HOST_USER, [email], fail_silently=False)
