from django.contrib import admin
from .models import Post, Category, Artist, Album

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    search_fields = ['title', 'content']
    list_filter = ['title']
    list_display = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    search_fields = ['title', 'subtitle']
    list_filter = ['title']

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
    search_fields = ['title', 'artist']
    list_filter = ['title']
    list_display = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
