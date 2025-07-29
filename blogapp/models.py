from django.db import models
from django.contrib.auth.models import User,BaseUserManager,UserManager,AbstractBaseUser

# Create your models here.
class Category(models.Model):
  category_name=models.CharField(max_length=50,unique=True)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural='Categories'

  def __str__(self):
    return self.category_name

STATUS_CHOICE=(
  ('draft','Draft'),
  ('published','Published')
)

class Blogs(models.Model):
  title=models.CharField(max_length=100,unique=True)
  slug=models.SlugField(unique=True,blank=True)
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  author=models.ForeignKey(User,on_delete=models.CASCADE)
  blog_image = models.ImageField()
  short_description=models.TextField(max_length=200)
  #blog_body=models.TextField()
  status=models.CharField(max_length=100,choices=STATUS_CHOICE,default='draft')
  is_featured=models.BooleanField(default=False)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name_plural='Blogs'

class Subscribe(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)

  def __str__(self):
    return self.email
  
class Contact(Subscribe):
  subject = models.TextField(max_length=200)
  phone = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  
  


