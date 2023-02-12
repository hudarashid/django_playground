from import_export import resources
from import_export.fields import Field
from .models import Blog


class BookResource(resources.ModelResource):

    blog_category = Field(column_name='category', attribute='blog_category__name')

    class Meta:
        model = Blog
        fields = ('title', 'body', 'blog_category', 'published_date',)