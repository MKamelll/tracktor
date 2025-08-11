from django.db import models
from user_profile import models as profile_models


# Create your models here.
class Post(models.Model):
    text = models.TextField()
    image = models.TextField(null=True)
    profile = models.ForeignKey(
        to=profile_models.Profile, on_delete=models.CASCADE, related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    text = models.TextField()
    image = models.TextField(null=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    profile = models.ForeignKey(
        to=profile_models.Profile, on_delete=models.CASCADE, related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Interaction(models.Model):
    pass
