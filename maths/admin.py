from django.contrib import admin

# maths/admin.py
from django.contrib import admin
from .models import Math, Result
# Register your models here.

admin.site.register(Math)
admin.site.register(Result)