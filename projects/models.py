from django.conf import settings
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(upload_to='uploads', height_field=None, width_field=None, max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    thumbnail = models.ImageField(blank=True, unique=True)

    def __str__(self):
        return self.title



