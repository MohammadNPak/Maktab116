from django.urls import path
from .views import PostDetailView
from .views import PostModelViewset,EditPostViewset,ReportUsersPostViewset
from rest_framework.routers import SimpleRouter

urlpatterns =[
    # path('posts',PostListView.as_view(),name="post-list"),
    path('posts_api/<int:pk>',PostDetailView.as_view(),name="post-detail"),
    # path('posts',PostView.as_view(),name="post-list")
]


router = SimpleRouter()
router.register("posts",PostModelViewset,basename='posts')
router.register("editpost",EditPostViewset,basename="editpost")
router.register("report",ReportUsersPostViewset,basename="report")
urlpatterns += router.urls
