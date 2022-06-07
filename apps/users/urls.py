from django.urls import path 
from apps.users.views import UserAPIView, RegisterView, UserUpdateAPIView, UserDeleteAPIView

urlpatterns = [
    #users api
    path('users', UserAPIView.as_view(), name = "users_api"),
    path('users/create', RegisterView.as_view(), name = "users_create_api"),
    path('users/update/<int:pk>', UserUpdateAPIView.as_view(), name = "users_update_api"),
    path('users/delete/<int:pk>', UserDeleteAPIView.as_view(), name = "users_delete_api"),
]