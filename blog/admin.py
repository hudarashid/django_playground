from django.contrib import admin
from .models import Blog, Category

class CategoryAdmin(admin.ModelAdmin):
    model = Category

    list_display = ('name', )
class BlogAdmin(admin.ModelAdmin):
    model = Blog

    list_display = ('title', 'body', 'published_date', 'created_date', 'edited_date','is_published',)
    
    field = ('title', 'body','blog_category', 'published_date', 'is_published',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
