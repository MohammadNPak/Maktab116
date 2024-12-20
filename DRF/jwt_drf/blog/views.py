from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwner
from django.contrib.auth import get_user_model
from .serializers import UserPostSerializer,UserPostSerializer2,UserPostSerializer3

from .tasks import test_task

User = get_user_model()

# class PostListView(APIView):
#     http_method_names = ["get", "post"]

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(data=serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={"message": "object is created successfully"},
#                             status=status.HTTP_201_CREATED)
#         else:
#             return Response(data={"message": "data is not valid"},
#                             status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):

    http_method_names = ["get","delete", "put","patch"]

    def get(self,request,pk):
        obj = get_object_or_404(Post,id=pk)
        test_task.delay(15)
        serializer = PostSerializer(obj)
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        obj = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(obj, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"message": "bad request"})
   
    def patch(self, request, pk):
        obj = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(obj, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"message": "bad request"})

    def delete(self, request, pk):
        obj = get_object_or_404(Post, id=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)


class PostModelViewset(ModelViewSet):
    # authentication_classes=[BasicAuthentication]
    permission_classes=[AllowAny]
    
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    http_method_names=["get","post","delete","patch","put"]

class EditPostViewset(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated,IsOwner]
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    http_method_names=["get","post","delete","patch","put"]
    
    
class ReportUsersPostViewset(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]
    queryset = User.objects.all()
    serializer_class=UserPostSerializer3
    http_method_names=["get"]