from django.shortcuts import render, get_object_or_404
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
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={"form": form, "posts": posts}
    )


def author_details(request,author_id):
    author = get_object_or_404(Author, pk=author_id)
    form = AuthorForm()
    return render(request, 'posts/author_details.html', {'author': author, "form": form})



def post_details(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"form": form, "posts": posts}
    )
