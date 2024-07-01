from django.urls import path
from blogapp.views import *

urlpatterns = [
    path('',home,name='index'),
    path('category/<int:category_id>/',category,name='catgeory'),
    path('blogs/<slug:slug>/',blogdeatil,name='blog'),
    path('blog-detail/search/',search,name='search'),
    path('register/',register,name='register'),
]


