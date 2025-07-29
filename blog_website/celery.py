import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_website.settings')

app = Celery('blog_website')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule={
    # 'send-mail-everyday-at-12.05':{
    #     'task':'mailfireapp.tasks.send_mail_func',
    #     'schedule':crontab(hour=12,minute=11)
    # },
    'send-newsletter-everyday-12-30': {
        'task': 'blogapp.tasks.send_newsletter_email',
        'schedule': crontab(hour=12, minute=59),
    }
}