from blog.resources import BookResource
from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Blog, Category

class CategoryAdmin(admin.ModelAdmin):
    model = Category

    list_display = ('name', )
class BlogAdmin(ExportActionMixin, admin.ModelAdmin):

    model = Blog

    resource_classes = [BookResource]

    list_display = ('title', 'body', 'published_date', 'created_date', 'edited_date','is_published',)
    
    field = ('title', 'body','blog_category', 'published_date', 'is_published',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
