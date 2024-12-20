from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializer

# @api_view(http_method_names=["GET"])
# def get_post(request):
#     obj = Post.objects.first()
#     serializer = PostSerializer(obj)

#     return Response(data=serializer.data)

class PostView(APIView):
    # permission_classes=[AllowAny]
    http_method_names=['get']
    def get(self,request):
        obj = Post.objects.first()
        serializer = PostSerializer(obj)
        return Response(data=serializer.data)
    