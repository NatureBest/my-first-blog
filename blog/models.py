from django.db import models
from django.contrib import admin
# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    tiemstamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tiemstamp')
admin.site.register(BlogsPost, BlogPostAdmin)
#admin.site.register(BlogsPost)