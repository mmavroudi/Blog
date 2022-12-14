from django.conf import settings
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    thumbnail = models.ImageField(blank=True, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    price = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(upload_to='uploads', height_field=None, width_field=None, max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Contact_Details(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name




