from django.db import models
from user_profile import models as profile_models
from themoviedb import models as themoviedb_models


# Create your models here.
class Post(models.Model):
    text = models.TextField()
    image = models.CharField(max_length=255, null=True)
    profile = models.ForeignKey(
        to=profile_models.Profile, on_delete=models.CASCADE, related_name="posts"
    )
    episode = models.ForeignKey(
        to=themoviedb_models.Episode, on_delete=models.CASCADE, related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    text = models.TextField()
    image = models.CharField(max_length=255, null=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    profile = models.ForeignKey(
        to=profile_models.Profile, on_delete=models.CASCADE, related_name="comments"
    )
    parent = models.ForeignKey(
        to="self", on_delete=models.CASCADE, related_name="replies", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Interaction(models.Model):
    class Type(models.TextChoices):
        LIKE = "like", "like"
        DISLIKE = "dislike", "dislike"

    kind = models.CharField(max_length=10, choices=Type.choices)
    comment = models.ForeignKey(
        to=Comment, on_delete=models.CASCADE, null=True, related_name="interactions"
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, null=True, related_name="interactions"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
