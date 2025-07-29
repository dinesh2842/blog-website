This is blog website where admin can post all the blogs and we can read those blogs.
there is a newsletter subscription and subscribed users get daily messages through their email
open cmd and activate virtualenv by using venv\Scripts\activate and then run the server python manage.py runserver
and start the celery worker celery -A blog_website worker --loglevel=info --pool=solo
we are using celery for sending mails and periodic tasks 
to run periodic tasks celery -A blog_website beat --loglevel=info
