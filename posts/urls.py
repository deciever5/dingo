from django.urls import path
from .views import authors_list,posts_list ,post_details ,author_details

app_name = "posts"

urlpatterns = [
    path('authors_list', authors_list),
    path('posts_list', posts_list),
    path('post_details', post_details),
    path('author_details', author_details),
]
