from django.contrib import admin

# Register your models here.
# maths/admin.py
from django.contrib import admin
from .models import Post, Author


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "author"]
    list_filter = ["author"]
    search_fields = ["author", "id"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'bio', 'email']
