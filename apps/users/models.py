from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(
        max_length=255,
        blank=True, null=True,
        db_index=True,
    )
    bio = models.CharField(
        max_length=255,
        blank=True, null=True,
    )
    profile_image = models.ImageField(
        upload_to='profile',
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.username} -- {self.email}"
