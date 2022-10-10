from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    slug = models.SlugField(blank=True, unique=True)