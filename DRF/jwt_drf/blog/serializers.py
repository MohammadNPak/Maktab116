from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=["id","title","body","created_at"]


class UserPostSerializer(serializers.ModelSerializer):
    post_set = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ["username","post_set"]

class UserPostSerializer2(serializers.ModelSerializer):
    post_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="posts-detail")
    
    class Meta:
        model = User
        fields = ["username","post_set"]

class UserPostSerializer3(serializers.ModelSerializer):
    post_set = PostSerializer(many=True,read_only=True)
    
    class Meta:
        model = User
        fields = ["username","post_set"]