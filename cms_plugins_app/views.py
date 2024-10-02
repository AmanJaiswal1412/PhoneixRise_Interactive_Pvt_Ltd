from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category


def blog_post_list(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'blog/blog_post_list.html', {'posts': posts})


def blog_post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_post_detail.html', {'post': post})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.blog_posts.all()
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})