from django.contrib import admin
from .models import Category,Blogs


class CategoryAdmin(admin.ModelAdmin):
  list_display=('id','category_name','created_at','updated_at')



class BlogAdmin(admin.ModelAdmin):
  list_display=('id','title','category','is_featured')
  prepopulated_fields={'slug':('title',)}
  search_fields=('id','title','category__category_name','status')
  list_editable=('is_featured',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogAdmin)
