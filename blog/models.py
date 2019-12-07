from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey('BlogCategory', null=True, blank=True, on_delete=False)
    slug = models.SlugField()
    
    def __str__(self):
        return '{} | {}'.format(self.get_cat_list(), self.title)

    def get_cat_list(self):
        k = self.category 
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        
        return breadcrumb[-1:0:-1]

    class Meta:
        ordering = ['-datePosted']

class BlogCategory(models.Model):
    category = models.CharField(max_length=300)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=True)

    class Meta:
        unique_together = ('slug', 'parent')    
        verbose_name_plural = "BlogCategory"     

    def __str__(self):                           
        full_path = [self.category]
        k = self.parent
        while k is not None:
            full_path.append(k.category)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        ordering = ['category', 'slug']