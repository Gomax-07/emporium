from django.db import models
from django.db.models import Model


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    image = models.ManyToManyField('Image', help_text='Select an image for this post')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class Image(models.Model):
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)


class Location(models.Model):
    location = models.CharField(max_length=150)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
