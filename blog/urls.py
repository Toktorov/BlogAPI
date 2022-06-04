"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.posts.views import PostAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView,PostCommentAPIView,PostCommentCreateAPIView,PostCommentUpdateAPIView,PostCommentDeleteAPIView
from apps.categories.views import CategoryAPIView,CategoryCreateAPIView,CategoryDeleteAPIView,CategoryUpdateAPIView
from apps.users.views import UserAPIView, UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    #post api
    path('api/posts', PostAPIView.as_view(), name = "post_api"),
    path('api/post/create', PostCreateAPIView.as_view(), name = "post_create_api"),
    path('api/post/update/<int:pk>', PostUpdateAPIView.as_view(), name = "post_api_update"),
    path('api/post/delete/<int:pk>', PostDeleteAPIView.as_view(), name = "post_api_delete"),

    #post_comment api
    path('api/post_comment',PostCommentAPIView.as_view(),name = "comment_api"),
    path('api/post_comment/create',PostCommentCreateAPIView.as_view(),name = "post_create_api"),
    path('api/post_comment/update/<int:pk>',PostCommentUpdateAPIView.as_view(),name = "post_api_update"),
    path('api/post_comment/delete/<int:pk>',PostCommentDeleteAPIView.as_view(),name = "post_api_delete"),

    #category api
    path('api/categories',CategoryAPIView.as_view(),name = "category_api"),
    path('api/category/create',CategoryCreateAPIView.as_view(),name = "category_create_api"),
    path('api/category/update/<int:pk>',CategoryUpdateAPIView.as_view(),name = "category_api_update"),
    path('api/category/delete/<int:pk>',CategoryDeleteAPIView.as_view(),name = "category_api_delete"),

    #users api
    path('api/users', UserAPIView.as_view(), name = "users_api"),
    path('api/users/create', UserCreateAPIView.as_view(), name = "users_create_api"),
    path('api/users/update/<int:pk>', UserUpdateAPIView.as_view(), name = "users_update_api"),
    path('api/users/delete/<int:pk>', UserDeleteAPIView.as_view(), name = "users_delete_api"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)