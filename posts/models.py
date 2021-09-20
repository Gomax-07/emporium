from django.db import models
from django.db.models import Model


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls, search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return Image


class Location(models.Model):
    location = models.CharField(max_length=150)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
