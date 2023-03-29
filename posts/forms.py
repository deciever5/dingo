from django import forms
from .models import Author, Post


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nick', 'bio', 'email']
