from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    picture = models.ImageField(
        upload_to="profile_picture",
        null=True, blank=True,
        default="profile_picture\profile.png")

    def get_absolute_url(self):
        return reverse("post_list")
    