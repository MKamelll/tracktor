from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    avatar = models.TextField(null=True)
    user = models.ForeignKey(to=User, related_name="profile", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
