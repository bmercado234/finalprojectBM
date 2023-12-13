# URLs for blog app

from django.urls import path
from . import views

# app namespace
app_name = 'blog'

urlpatterns = [
    # root
    path('', views.blog_list, name='blog_list'),
    # Map to create post view
    path('create/', views.create_post, name='create_post'),
    # Use post id to map to urls of post
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    # Use post id to map to urls of comment
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),
    # use post id to map to urls of like
    path('<int:post_id>/like/', views.like_post, name='like_post'),
]