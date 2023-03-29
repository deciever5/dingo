from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
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
    bio = models.TextField(blank=True, max_length=1024, validators=[MaxLengthValidator(1024, message="Bio za długie")])
    email = models.EmailField(max_length=30, blank=True, unique=True)


    def __str__(self):
        email_str = f" ({self.email})" if self.email else ""
        bio_str = f" - {self.bio[:50]}..." if self.bio else ""
        return f"{self.nick}{email_str}{bio_str}"

    def save(self, *args, **kwargs):
        self.full_clean()

        super(Author, self).save(*args, **kwargs)

