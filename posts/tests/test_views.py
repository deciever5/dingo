from django.test import TestCase, Client
from posts.models import Author, Post


class PostsViewsTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(nick="John", bio="Bio text", email="john@example.com")
        self.post = Post.objects.create(title="Test Post", content="Test content", author=self.author)
        self.client = Client()

    def test_authors_list(self):
        response = self.client.get("/posts/authors_list")
        self.assertEqual(response.status_code, 200)
        self.assertIn("John", response.content.decode())

    def test_posts_list(self):
        response = self.client.get("/posts/posts_list")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Post", response.content.decode())

    def test_author_details(self):
        response = self.client.get(f"/posts/author_details/{self.author.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("John", response.content.decode())

    def test_post_details(self):
        response = self.client.get("/posts/post_details")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Post", response.content.decode())
