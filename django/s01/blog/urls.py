from django.urls import path
from .views import post_detail_view,posts_list_view

urlpatterns = [
    path('post/<int:pk>',post_detail_view,name="post_detail"),
    path('post',posts_list_view,name="post_list"),
]
