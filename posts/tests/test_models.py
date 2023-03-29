from django.core.exceptions import ValidationError
from django.test import TestCase
from posts.models import Author, Post


class AuthorModelTest(TestCase):

    def test_author_creation(self):
        author = Author.objects.create(nick="John", bio="Bio text", email="john@example.com")
        self.assertEqual(author.nick, "John")
        self.assertEqual(author.bio, "Bio text")
        self.assertEqual(author.email, "john@example.com")

    def test_author_str_method(self):
        author = Author.objects.create(nick="John", bio="Bio text", email="john@example.com")
        self.assertEqual(str(author), "John (john@example.com) - Bio text...")

    def test_author_save_validates_bio_length(self):
        long_bio = "a" * 1025
        author = Author(nick="John", bio=long_bio, email="john@example.com")
        with self.assertRaisesRegex(ValidationError, "Bio cannot be longer than 1024 characters"):
            author.save()


class PostModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(nick="John", bio="Bio text", email="john@example.com")

    def test_post_creation(self):
        post = Post.objects.create(title="Test Post", content="Test content for post", author=self.author)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "Test content for post")
        self.assertEqual(post.author, self.author)

    def test_post_str_method(self):
        post = Post.objects.create(title="Test Post", content="Test content for post", author=self.author)
        expected_str = (
            f"Title: {post.title}\n"
            f"Content: {post.content}\n"
            f"Created: {post.created}\n"
            f"Modified: {post.modified}\n"
            f"Author: {post.author}"
        )
        self.assertEqual(str(post), expected_str)
