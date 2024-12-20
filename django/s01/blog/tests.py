from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user,get_user_model
# from django.contrib.auth.models import User
# Create your tests here.
from blog.models import Post

class TestPost(TestCase):

    def setUp(self):
        self.credential = {"username":"abc","password":"Zaq11qaZ"}
        self.user = get_user_model().objects.create_user(**self.credential)

        # return super().setUp()

    
    def test_create_post(self):
        post_data = {"title":"first post","body":"body","author":self.user}
        post = Post.objects.create(**post_data)
        self.assertEqual(Post.objects.all().count(),1)
        self.assertEqual(Post.objects.first().author.username,self.credential.username)
    
    