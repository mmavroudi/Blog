from django.contrib import admin
from .models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    search_fields = ['title', 'content']
    list_filter = ['title']
    list_display = ['title', 'content']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    search_fields = ['title', 'subtitle']
    list_filter = ['title']

