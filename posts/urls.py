from django.urls import path
from .views import (
    posts_list,
    post_details,
    authors_list,
    author_details,
)


app_name = "posts"

urlpatterns = [
    path("", posts_list, name="posts_list"),
    path("posts/p/<int:id>", post_details, name="details"),
    path("posts/authors_list", authors_list, name="authors_list"),
    path("posts/a/<int:id>", author_details, name="author_details"),
]
