from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_post_list, name='blog_post_list'),
    path('blog/<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
]