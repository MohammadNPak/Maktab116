from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    body=models.TextField()
    