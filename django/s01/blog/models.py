from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
<<<<<<< HEAD
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        
        # ,related_name="user_posts"
        )
    like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="post_like")
=======
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

>>>>>>> 89a7a0ed935605cb33d82b45e3dfd52be86f1efa
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_add_comment","can add a comment under this post")
        ]
    
    def __str__(self) -> str:
        return f"Post(Title: {self.title[:10]})"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
<<<<<<< HEAD

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    # parent = GenericForeignKey()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    

=======
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    parent = GenericForeignKey("content_type","object_id")
>>>>>>> 89a7a0ed935605cb33d82b45e3dfd52be86f1efa
    