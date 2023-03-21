from django import forms
from .models import Author


class PostForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(required=True)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=True)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nick', 'bio', 'email']
