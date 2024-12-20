from django.urls import path
<<<<<<< HEAD
from . import views


urlpatterns = [
    path('post/<int:pk>/add_comment',views.CreateCommentView.as_view(),name="create_comment"),
    path('post/<int:pk>/like',views.LikePost.as_view(),name="like_post"),
    path('post/<int:pk>',views.post_detail_view,name="post_detail"),
    path('post',views.posts_list_view,name="post_list"),
    path('search_results',views.SearchResultsView.as_view(),name="search_results"),
=======
from .views import post_detail_view,posts_list_view,CreateCommentView

urlpatterns = [
    path('post/<int:pk>',post_detail_view,name="post_detail"),
    path('post',posts_list_view,name="post_list"),
    path('create_comment/<str:content_type>/<int:object_id>/'
         ,CreateCommentView.as_view()
         ,name="create_comment"),
>>>>>>> 89a7a0ed935605cb33d82b45e3dfd52be86f1efa
]
