from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
             DRAFT = 'DF', 'Draft'
             PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=250, null=True)
    body = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now, null=True)
    create = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(choices=Status.choices, default=Status.DRAFT, null=True, max_length=2)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='blog_posts')

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id])
    