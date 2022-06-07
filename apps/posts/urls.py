from django.urls import path 
from apps.posts.views import PostAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView,PostCommentAPIView,PostCommentCreateAPIView,PostCommentUpdateAPIView,PostCommentDeleteAPIView

urlpatterns = [
    #post api
    path('posts', PostAPIView.as_view(), name = "post_api"),
    path('post/create', PostCreateAPIView.as_view(), name = "post_create_api"),
    path('post/update/<int:pk>', PostUpdateAPIView.as_view(), name = "post_api_update"),
    path('post/delete/<int:pk>', PostDeleteAPIView.as_view(), name = "post_api_delete"),

    #post_comment api
    path('post_comment',PostCommentAPIView.as_view(),name = "comment_api"),
    path('post_comment/create',PostCommentCreateAPIView.as_view(),name = "post_create_api"),
    path('post_comment/update/<int:pk>',PostCommentUpdateAPIView.as_view(),name = "post_api_update"),
    path('post_comment/delete/<int:pk>',PostCommentDeleteAPIView.as_view(),name = "post_api_delete"),
]