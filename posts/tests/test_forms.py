from django.test import TestCase
from posts.forms import PostForm, AuthorForm
from posts.models import Author, Post
from django.core.exceptions import ValidationError


class PostFormTest(TestCase):

    def test_form_has_fields(self):
        form = PostForm()
        self.assertIn('title', form.fields)
        self.assertIn('content', form.fields)
        self.assertIn('author', form.fields)

    def test_form_valid_data(self):
        author = Author.objects.create(nick="John", bio="Bio text", email="john@example.com")
        form_data = {'title': 'Test Post', 'content': 'Test text for post', 'author': author.pk}
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


class AuthorModelTest(TestCase):
    def test_save_bio_too_long(self):
        nick = "TestTooLong"
        bio = "A" * 1025
        email = "test@example.com"
        author = Author(nick=nick, bio=bio, email=email)

        with self.assertRaises(ValidationError):
            author.save()

    def test_save_bio_not_too_long(self):
        nick = "TestNotTooLong"
        bio = "A" * 1024
        email = "test@example.com"

        author = Author(nick=nick, bio=bio, email=email)

        try:
            author.save()

        except ValidationError:
            self.fail("ValidationError raised but it shouldn't ")
        # Check that the author was saved to the database
        saved_author = Author.objects.get(nick=nick)
        self.assertEqual(saved_author.bio, bio)
