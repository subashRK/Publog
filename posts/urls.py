from django.urls import path
from .views import *

urlpatterns = [
    path("all/", home, name="all_posts"),
    path("add/", add_post, name="add_post"),
    path("view/<int:id>/", post_detail, name="post_detail"),
    path("edit/<int:id>/", edit_post, name="edit_post"),
    path("delete/<int:id>/", delete_post, name="delete_post"),
    path("followers-posts/", followers_posts, name="followers_posts"),
    path("like/<int:id>/", like_post, name="like_post"),
    path("comment/add/<int:id>/", add_comment, name="add_comment"),
    path("comment/edit/<int:id>/", edit_comment, name="edit_comment"),
    path("comment/delete/<int:id>/", delete_comment, name="delete_comment"),
    path("comment/like/<int:id>/", like_comment, name="like_comment"),
    path("user/<int:id>/", user_posts, name="user_posts"),
]