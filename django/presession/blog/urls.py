from django.urls import path
from .views import post_detail_view,posts_list_view,SearchResultView

urlpatterns = [
    path('post/<int:pk>',post_detail_view,name="post_detail"),
    path('post',posts_list_view,name="post_list"),
    path('search_results',SearchResultView.as_view(),name="search_results"),
]
