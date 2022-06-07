from django.urls import path
from apps.categories.views import CategoryAPIView,CategoryCreateAPIView,CategoryDeleteAPIView,CategoryUpdateAPIView

urlpatterns = [
    #category api
    path('categories',CategoryAPIView.as_view(),name = "category_api"),
    path('category/create',CategoryCreateAPIView.as_view(),name = "category_create_api"),
    path('category/update/<int:pk>',CategoryUpdateAPIView.as_view(),name = "category_api_update"),
    path('category/delete/<int:pk>',CategoryDeleteAPIView.as_view(),name = "category_api_delete"),
]