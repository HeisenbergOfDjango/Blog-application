from django.contrib import admin

from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'author', 'publish', 'status']
    search_fields = ['title', 'id']
    prepopulated_fields = {'slug' : ('title',)}