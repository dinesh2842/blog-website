from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from blog_website import settings

@shared_task(bind=True)
def send_mail_func(self):
    users=get_user_model().objects.all()
    for user in users:
        mail_subject='welcome to Tech Blogs'
        message='new blogs are released dont forget to watch the blogs'
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,

        )
    return 'Email sent successfully to all the users'