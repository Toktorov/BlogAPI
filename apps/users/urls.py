from rest_framework.routers import DefaultRouter

from apps.users import views

router = DefaultRouter()
router.register('', views.UserAPIViewSet, basename='users')

urlpatterns = router.urls
