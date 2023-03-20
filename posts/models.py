from django.core.exceptions import ValidationError
from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Post(TimeStampedModel):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=1024)
    author = models.ForeignKey('posts.Author', on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Content: {self.content}\n"
            f"Created: {self.created}\n"
            f"Modified: {self.modified}\n"
            f"Author: {self.author}"
        )


class Author(models.Model):
    nick = models.CharField(max_length=15, unique=True)
    bio = models.TextField(blank=True, max_length=1024)
    email = models.EmailField(max_length=30, blank=True, unique=True)

    def __str__(self):
        return self.nick

    def save(self, *args, **kwargs):
        # Validate bio max_length before saving
        if self.bio and len(self.bio) > 1024:
            raise ValidationError("Bio cannot be longer than 1024 characters")

        super(Author, self).save(*args, **kwargs)
