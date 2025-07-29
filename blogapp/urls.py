from django.urls import path
from blogapp.views import *

urlpatterns = [
    path('',home,name='index'),
    path('category/<int:category_id>/',category,name='catgeory'),
    path('blogs/<slug:slug>/',blogdeatil,name='blog'),
    path('blog-detail/search/',search,name='search'),
    path('register/',register,name='register'),
    path('subscribe/',news_letter_subscription,name='subscribe'),
    #path('testview',testview,name='testview'),
    path('sendmail/',send_mail_to_all_users,name='send_mail'),
    path('contact',contact,name='contact')
]


