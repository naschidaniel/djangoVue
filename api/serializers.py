from rest_framework import serializers
from blog.models import BlogPost, BlogCategory
from pages.models import Pages

## Blog
class BlogPostSerializer(serializers.ModelSerializer):
    datePosted = serializers.DateTimeField(format='%Y-%m-%d %H:%M', input_formats=None)
    param = 'djfaödsj'
    class Meta:
        model = BlogPost
        many = True
        fields = ['title', 'content', 'datePosted', 'author', 'category']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'category', 'slug', 'parent']

## Pages
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ['title', 'content', 'datePosted']