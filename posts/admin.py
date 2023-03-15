from django.contrib import admin

# Register your models here.
# maths/admin.py
from django.contrib import admin
from .models import Post,Author
# Register your models here.

admin.site.register(Post)
admin.site.register(Author)