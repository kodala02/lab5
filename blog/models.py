from django.contrib.auth.models import User
from django.db import models


class PostManager(models.Manager):
    def public_posts(self):
        return self.filter(is_public=True)


class Post(models.Model):
    # Your Post model fields go here
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    objects = PostManager()

    def __str__(self):
        return f"{self.posted_by.username} - {self.created_at}"
