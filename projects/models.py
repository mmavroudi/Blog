from django.conf import settings
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
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
    slug = models.SlugField(null=False, unique=True)
    tags = TaggableManager()
    pub_date = models.DateField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_post", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Contact_Details(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads', height_field=None, width_field=None, max_length=100)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=60)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    release_date = models.DateField()
    size = models.IntegerField()
    image = models.ImageField(upload_to='uploads', height_field=None, width_field=None, max_length=100)
    price = models.IntegerField()
    slug = models.SlugField(null=False, unique=True)
    tags = TaggableManager()
    TYPE_CHOICES = [
        ('VINYL', 'Vinyl'),
        ('DIGITAL', 'Digital'),
    ]
    type_album = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES,
        default='VINYL',
    )
    STOCK_CHOICES = [
        ('INSTOCK', 'In Stock'),
        ('OUTOFSTOCK', 'Out of Stock'),
    ]
    stock = models.CharField(
        max_length=10,
        choices=STOCK_CHOICES,
        default='OUTOFSTOCK',
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("album_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
