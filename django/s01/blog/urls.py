from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:pk>/add_comment',views.CreateCommentView.as_view(),name="create_comment"),
    path('post/<int:pk>/like',views.LikePost.as_view(),name="like_post"),
    path('post/<int:pk>',views.post_detail_view,name="post_detail"),
    path('post',views.posts_list_view,name="post_list"),
    path('search_results',views.SearchResultsView.as_view(),name="search_results"),
]
