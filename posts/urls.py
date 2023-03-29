from django.urls import path
from .views import authors_list,posts_list ,post_details ,author_details

app_name = "posts"

urlpatterns = [
    path('authors_list', authors_list,name='authors_list'),
    path('posts_list', posts_list,name='posts_list'),
    path('post_details/<int:pk>/', post_details, name='post_details'),
    path('author_details/<int:author_id>/', author_details, name='author_details'),
]
