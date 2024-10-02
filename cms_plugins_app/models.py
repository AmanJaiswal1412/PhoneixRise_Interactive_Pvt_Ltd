from django.db import models
from cms.models.pluginmodel import CMSPlugin
from cms.models import Page
from django.contrib.auth.models import User  # Using Django's built-in User model


class PageBannersModel(CMSPlugin):
    page_title = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name="Page", related_name="linked_pages")
    banner_images = models.ImageField(upload_to='images/page_banners')

    def __str__(self):
        return self.page.get_title()


class ProductTechnologyModel(CMSPlugin):
    tech_title = models.TextField(max_length=200, default='Technology', null=False)
    tech_description = models.TextField(max_length=200, default='Technology Description', null=False)
    tech_icon = models.ImageField(upload_to='images/tech_icons')
    associated_page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name="Associated Page",
                                        related_name="tech_product")

    def __str__(self):
        return self.tech_title


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blog_posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")  # Add author field

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Or allow anonymous comments by removing this
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

