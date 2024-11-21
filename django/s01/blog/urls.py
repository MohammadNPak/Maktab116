from django.urls import path
from .views import post_detail_view,posts_list_view,CreateCommentView

urlpatterns = [
    path('post/<int:pk>',post_detail_view,name="post_detail"),
    path('post',posts_list_view,name="post_list"),
    path('create_comment/<str:content_type>/<int:object_id>/'
         ,CreateCommentView.as_view()
         ,name="create_comment"),
]
