from django.urls import path
# from .views import get_post
from .views import PostView

urlpatterns = [
    path("post",PostView.as_view(),name='post-detail'),
]