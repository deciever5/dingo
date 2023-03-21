from django.shortcuts import render
from .models import Author, Post
from .forms import AuthorForm,PostForm


# Create your views here.
def authors_list(request):
    authors = Author.objects.all()
    form = AuthorForm()
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={"form": form, "authors": authors}
    )


def posts_list(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={"form": form, "posts": posts}
    )


def author_details(request):
    authors = Author.objects.all()
    form = AuthorForm()
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={"form": form, "authors": authors}
    )


def post_details(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"form": form, "posts": posts}
    )
