from django.test import TestCase
from posts.forms import PostForm, AuthorForm
from posts.models import Author, Post

class PostFormTest(TestCase):

    def test_form_has_fields(self):
        form = PostForm()
        self.assertIn('title', form.fields)
        self.assertIn('text', form.fields)
        self.assertIn('author', form.fields)

    def test_form_valid_data(self):
        author = Author.objects.create(nick="John", bio="Bio text", email="john@example.com")
        form_data = {'title': 'Test Post', 'text': 'Test text for post', 'author': author.pk}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {'title': '', 'text': '', 'author': ''}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())


class AuthorFormTest(TestCase):

    def test_form_has_fields(self):
        form = AuthorForm()
        self.assertIn('nick', form.fields)
        self.assertIn('bio', form.fields)
        self.assertIn('email', form.fields)

    def test_form_valid_data(self):
        form_data = {'nick': 'John', 'bio': 'Bio text', 'email': 'john@example.com'}
        form = AuthorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {'nick': '', 'bio': '', 'email': ''}
        form = AuthorForm(data=form_data)
        self.assertFalse(form.is_valid())
