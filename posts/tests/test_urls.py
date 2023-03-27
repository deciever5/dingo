from django.urls import resolve
from django.urls.exceptions import Resolver404
from unittest import TestCase
from posts.views import authors_list, posts_list, post_details, author_details

class TestUrls(TestCase):

    def test_resolution_for_authors_list(self):
        resolver = resolve('/posts/authors_list')
        self.assertEqual(resolver.func, authors_list)

    def test_resolution_for_posts_list(self):
        resolver = resolve('/posts/posts_list')
        self.assertEqual(resolver.func, posts_list)

    def test_resolution_for_post_details(self):
        resolver = resolve('/posts/post_details')
        self.assertEqual(resolver.func, post_details)

    def test_resolution_for_author_details(self):
        resolver = resolve('/posts/author_details/1/')
        self.assertEqual(resolver.func, author_details)
        self.assertEqual(resolver.kwargs, {'author_id': 1})

    def test_resolution_for_invalid_urls(self):
        with self.assertRaises(Resolver404):
            resolve('/posts/nonexistent_url')
