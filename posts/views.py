from django.shortcuts import render, get_object_or_404,redirect
from .models import Author, Post
from .forms import AuthorForm,PostForm


# Create your views here.
def authors_list(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()

    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={"form": form, "authors": authors, "title": "Authors list"}
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
        context={"form": form, "posts": posts, "title": "Posts list"}
    )


def author_details(request,author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'posts/author_details.html', {'author': author, 'title': 'Author details'})



def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"post": post, "title": "Post details"}
    )
