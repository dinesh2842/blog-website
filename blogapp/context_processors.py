from .models import *

def get_categories(request):
  categories=Category.objects.all()
  return dict(categories=categories)