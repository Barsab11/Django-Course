from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish','status')
    prepopulated_fields = {"slug": ["title"]}