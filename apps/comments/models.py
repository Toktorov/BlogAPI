from django.contrib.auth import get_user_model
from django.db import models

from apps.posts.models import Post

User = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.post.id}"

    class Meta:
        ordering = ['-comment_created']
