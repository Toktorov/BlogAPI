from tabnanny import verbose
from django.db import models
from apps.categories.models import Category
from apps.users.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'post_image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, related_name="category")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text 

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
