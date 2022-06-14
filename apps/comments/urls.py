from rest_framework.routers import DefaultRouter
from apps.comments import views

router = DefaultRouter()
router.register('comments', views.CommentAPIViewSet, basename='comment')

urlpatterns = router.urls
