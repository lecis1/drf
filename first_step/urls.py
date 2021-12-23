from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from first_step.viewsets.user import UserViewSet, GroupViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = router.urls
