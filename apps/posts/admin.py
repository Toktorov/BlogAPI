from django.contrib import admin
from apps.posts.models import Post, PostComment
# Register your models here.

admin.site.register(Post)
admin.site.register(PostComment)