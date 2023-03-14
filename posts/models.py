from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey('posts.Author', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    nick = models.CharField(max_length=15, unique=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nick
